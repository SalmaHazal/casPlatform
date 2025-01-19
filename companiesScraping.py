import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.charika.ma/societes-"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def scrape_data(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    data_list = []

    companies = soup.find_all("div", class_="text-soc col-md-10 col-sm-10 col-xs-10 nopaddingright")
    for company in companies:
        name = company.find("a", class_="goto-fiche").get_text(strip=True) if company.find("a", class_="goto-fiche") else None

        sector = None
        sectorAll = company.find('div', class_='truncate-m ellipsis')
        if sectorAll:
            p_tag = sectorAll.find('p')
            if p_tag:
                for b in p_tag.find_all('b'):
                    b.extract()
                sector = p_tag.get_text(strip=True)

        address = company.find("label").get_text(strip=True) if company.find("label") else None

        data_list.append({
            "Company Name": name,
            "Sector of Activity": sector,
            "Address": address
        })

    return data_list


def save_to_json(data, filename="companies.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    all_data = []

    for i in range(1, 90444):
        url = f"{BASE_URL}{i}"
        print(f"Scraping page {i}: {url}")
        page_data = scrape_data(url)
        all_data.extend(page_data)
        if i % 1000 == 0:
            save_to_json(all_data, filename=f"companies_part_{i}.json")

    # Save all data into a single JSON file
    save_to_json(all_data, filename="all_companies.json")

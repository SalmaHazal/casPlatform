import json
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load companies from JSON file
with open('companies.json', 'r', encoding='utf-8') as file:
    companies = json.load(file)

# Project metadata
project = {
    "Theme": "Recycling and eco-friendly products",
    "Location": "Azilal",
    "Required Support": "A humanitarian caravan requires a variety of materials to provide effective support in crisis situations. Essential supplies include food and water (non-perishable items and bottled water), medical supplies (first aid kits, medicines, PPE), hygiene products (soap, toothpaste, sanitary pads), and clothing (weather-appropriate attire, blankets, and sleeping bags). Logistical materials such as transportation (vehicles, fuel), shelters (tents, tarps), cooking equipment (stoves, fuel), and storage containers are crucial for organizing and delivering aid. Communication tools (radios, satellite phones), safety gear (helmets, vests), and security measures (emergency protocols) ensure smooth operations. Additionally, documentation for registration, maps, and identification are important for managing the relief effort. Depending on the specific needs of the region, specialized items such as childcare materials, school supplies, and farming tools may also be required. Coordination with local authorities ensures the caravan's efficiency in reaching and assisting those in need."
}

# Extract company sectors and project theme
project_theme = project["Required Support"]
company_sectors = [company["Sector of Activity"] for company in companies]

# Encode the project theme and company sectors into embeddings
project_embedding = model.encode(project_theme, convert_to_tensor=True)
company_embeddings = model.encode(company_sectors, convert_to_tensor=True)

# Compute cosine similarity
similarities = util.cos_sim(project_embedding, company_embeddings)

# Rank companies by similarity score
ranked_companies = sorted(
    zip(companies, similarities[0].tolist()),
    key=lambda x: x[1],
    reverse=True
)

# Print suggestions
for company, score in ranked_companies:
    print(f"Company: {company['Company Name']}, Similarity: {score:.2f}")

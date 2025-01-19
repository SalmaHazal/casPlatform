import json
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# Load companies from JSON file
# with open('companies.json', 'r', encoding='utf-8') as file:
#     companies = json.load(file)

companies = [
    {
      "Company Name": "Kamar catering (ste)",
      "Sector of Activity": "Boulangerie, patisserie, glacier, milk-bar et cafeterie",
      "Address": "Rue abou alae el maari residence tissir n7-8 - Tanger-Assilah"
    },
    {
      "Company Name": "Boustan transport (ste al)",
      "Sector of Activity": "Transport routier",
      "Address": "20 amr ibn al ass n2 - Tanger-Assilah"
    },
    {
      "Company Name": "Socimag (ste)",
      "Sector of Activity": "- travaux de bâtiments - travaux de plomberie et d'électricité",
      "Address": "5 rue bilal - Tanger-Assilah"
    },
    {
      "Company Name": "Trafu boughaz (ste)",
      "Sector of Activity": "Import export",
      "Address": "Rue p n4 el boughaz - Tanger-Assilah"
    },
    {
      "Company Name": "Niuyn negoce (ste)",
      "Sector of Activity": "Import export, negoce en general",
      "Address": "1 rue farabi n3 - Tanger-Assilah"
    },
    {
      "Company Name": "Ibra textile",
      "Sector of Activity": "- commerce de fibres textiles",
      "Address": "Zone industrielle al majd lot 853, bp 1155 - Tanger-Assilah"
    },
    {
      "Company Name": "Detroit (chantier du)",
      "Sector of Activity": "Ese de construction et travaux publics",
      "Address": "Florensia tranche 2 rue irak n 6 - Tanger-Assilah"
    },
    {
      "Company Name": "Electro construction industrielle le but (ECIB)",
      "Sector of Activity": "Electricite industrielle, construction, genie civil, construction metallique et plomberie",
      "Address": "Hay saada 4 rue 45 n6 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Eolienne (ste d'ingenierie)",
      "Sector of Activity": "Ingenierie, etudes techniques",
      "Address": "7 rue de mexique - Tanger-Assilah"
    },
    {
      "Company Name": "Achhab binaa (ste)",
      "Sector of Activity": "Construction et promotion immobiliere",
      "Address": "5 rue l'hopital espagnol n9 - Tanger-Assilah"
    },
    {
      "Company Name": "Boustan transport (ste al)",
      "Sector of Activity": "Transport routier",
      "Address": "20 amr ibn al ass n2 - Tanger-Assilah"
    },
    {
      "Company Name": "Socimag (ste)",
      "Sector of Activity": "- travaux de bâtiments - travaux de plomberie et d'électricité",
      "Address": "5 rue bilal - Tanger-Assilah"
    },
    {
      "Company Name": "Trafu boughaz (ste)",
      "Sector of Activity": "Import export",
      "Address": "Rue p n4 el boughaz - Tanger-Assilah"
    },
    {
      "Company Name": "Niuyn negoce (ste)",
      "Sector of Activity": "Import export, negoce en general",
      "Address": "1 rue farabi n3 - Tanger-Assilah"
    },
    {
      "Company Name": "Ibra textile",
      "Sector of Activity": "- commerce de fibres textiles",
      "Address": "Zone industrielle al majd lot 853, bp 1155 - Tanger-Assilah"
    },
    {
      "Company Name": "Detroit (chantier du)",
      "Sector of Activity": "Ese de construction et travaux publics",
      "Address": "Florensia tranche 2 rue irak n 6 - Tanger-Assilah"
    },
    {
      "Company Name": "Electro construction industrielle le but (ECIB)",
      "Sector of Activity": "Electricite industrielle, construction, genie civil, construction metallique et plomberie",
      "Address": "Hay saada 4 rue 45 n6 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Eolienne (ste d'ingenierie)",
      "Sector of Activity": "Ingenierie, etudes techniques",
      "Address": "7 rue de mexique - Tanger-Assilah"
    },
    {
      "Company Name": "Achhab binaa (ste)",
      "Sector of Activity": "Construction et promotion immobiliere",
      "Address": "5 rue l'hopital espagnol n9 - Tanger-Assilah"
    },
    {
      "Company Name": "Schengen tex (ste)",
      "Sector of Activity": "Confection des vetements et tous articles de pret-a-porter",
      "Address": "Rue khansae n18 castilla - Tanger-Assilah"
    },
    {
      "Company Name": "Socimag (ste)",
      "Sector of Activity": "- travaux de bâtiments - travaux de plomberie et d'électricité",
      "Address": "5 rue bilal - Tanger-Assilah"
    },
    {
      "Company Name": "Trafu boughaz (ste)",
      "Sector of Activity": "Import export",
      "Address": "Rue p n4 el boughaz - Tanger-Assilah"
    },
    {
      "Company Name": "Niuyn negoce (ste)",
      "Sector of Activity": "Import export, negoce en general",
      "Address": "1 rue farabi n3 - Tanger-Assilah"
    },
    {
      "Company Name": "Ibra textile",
      "Sector of Activity": "- commerce de fibres textiles",
      "Address": "Zone industrielle al majd lot 853, bp 1155 - Tanger-Assilah"
    },
    {
      "Company Name": "Detroit (chantier du)",
      "Sector of Activity": "Ese de construction et travaux publics",
      "Address": "Florensia tranche 2 rue irak n 6 - Tanger-Assilah"
    },
    {
      "Company Name": "Electro construction industrielle le but (ECIB)",
      "Sector of Activity": "Electricite industrielle, construction, genie civil, construction metallique et plomberie",
      "Address": "Hay saada 4 rue 45 n6 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Eolienne (ste d'ingenierie)",
      "Sector of Activity": "Ingenierie, etudes techniques",
      "Address": "7 rue de mexique - Tanger-Assilah"
    },
    {
      "Company Name": "Achhab binaa (ste)",
      "Sector of Activity": "Construction et promotion immobiliere",
      "Address": "5 rue l'hopital espagnol n9 - Tanger-Assilah"
    },
    {
      "Company Name": "Schengen tex (ste)",
      "Sector of Activity": "Confection des vetements et tous articles de pret-a-porter",
      "Address": "Rue khansae n18 castilla - Tanger-Assilah"
    },
    {
      "Company Name": "Boutaour",
      "Sector of Activity": "Import export",
      "Address": "1 rue el moutanabi - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Trafu boughaz (ste)",
      "Sector of Activity": "Import export",
      "Address": "Rue p n4 el boughaz - Tanger-Assilah"
    },
    {
      "Company Name": "Niuyn negoce (ste)",
      "Sector of Activity": "Import export, negoce en general",
      "Address": "1 rue farabi n3 - Tanger-Assilah"
    },
    {
      "Company Name": "Ibra textile",
      "Sector of Activity": "- commerce de fibres textiles",
      "Address": "Zone industrielle al majd lot 853, bp 1155 - Tanger-Assilah"
    },
    {
      "Company Name": "Detroit (chantier du)",
      "Sector of Activity": "Ese de construction et travaux publics",
      "Address": "Florensia tranche 2 rue irak n 6 - Tanger-Assilah"
    },
    {
      "Company Name": "Electro construction industrielle le but (ECIB)",
      "Sector of Activity": "Electricite industrielle, construction, genie civil, construction metallique et plomberie",
      "Address": "Hay saada 4 rue 45 n6 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Eolienne (ste d'ingenierie)",
      "Sector of Activity": "Ingenierie, etudes techniques",
      "Address": "7 rue de mexique - Tanger-Assilah"
    },
    {
      "Company Name": "Achhab binaa (ste)",
      "Sector of Activity": "Construction et promotion immobiliere",
      "Address": "5 rue l'hopital espagnol n9 - Tanger-Assilah"
    },
    {
      "Company Name": "Schengen tex (ste)",
      "Sector of Activity": "Confection des vetements et tous articles de pret-a-porter",
      "Address": "Rue khansae n18 castilla - Tanger-Assilah"
    },
    {
      "Company Name": "Boutaour",
      "Sector of Activity": "Import export",
      "Address": "1 rue el moutanabi - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Boughaz (informatique conceptions systeme) (ICSB)",
      "Sector of Activity": "Commerce de prestation en informatique",
      "Address": "7 rue khalid ibn el oualid n12 - Tanger-Assilah"
    },
    {
      "Company Name": "Niuyn negoce (ste)",
      "Sector of Activity": "Import export, negoce en general",
      "Address": "1 rue farabi n3 - Tanger-Assilah"
    },
    {
      "Company Name": "Ibra textile",
      "Sector of Activity": "- commerce de fibres textiles",
      "Address": "Zone industrielle al majd lot 853, bp 1155 - Tanger-Assilah"
    },
    {
      "Company Name": "Detroit (chantier du)",
      "Sector of Activity": "Ese de construction et travaux publics",
      "Address": "Florensia tranche 2 rue irak n 6 - Tanger-Assilah"
    },
    {
      "Company Name": "Electro construction industrielle le but (ECIB)",
      "Sector of Activity": "Electricite industrielle, construction, genie civil, construction metallique et plomberie",
      "Address": "Hay saada 4 rue 45 n6 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Eolienne (ste d'ingenierie)",
      "Sector of Activity": "Ingenierie, etudes techniques",
      "Address": "7 rue de mexique - Tanger-Assilah"
    },
    {
      "Company Name": "Achhab binaa (ste)",
      "Sector of Activity": "Construction et promotion immobiliere",
      "Address": "5 rue l'hopital espagnol n9 - Tanger-Assilah"
    },
    {
      "Company Name": "Schengen tex (ste)",
      "Sector of Activity": "Confection des vetements et tous articles de pret-a-porter",
      "Address": "Rue khansae n18 castilla - Tanger-Assilah"
    },
    {
      "Company Name": "Boutaour",
      "Sector of Activity": "Import export",
      "Address": "1 rue el moutanabi - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Boughaz (informatique conceptions systeme) (ICSB)",
      "Sector of Activity": "Commerce de prestation en informatique",
      "Address": "7 rue khalid ibn el oualid n12 - Tanger-Assilah"
    },
    {
      "Company Name": "Sorenav",
      "Sector of Activity": "Approvisionnement, ravitaillement, nettoyage des navires",
      "Address": "Rue marseille, résidence la madrague n° 4 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Ibra textile",
      "Sector of Activity": "- commerce de fibres textiles",
      "Address": "Zone industrielle al majd lot 853, bp 1155 - Tanger-Assilah"
    },
    {
      "Company Name": "Detroit (chantier du)",
      "Sector of Activity": "Ese de construction et travaux publics",
      "Address": "Florensia tranche 2 rue irak n 6 - Tanger-Assilah"
    },
    {
      "Company Name": "Electro construction industrielle le but (ECIB)",
      "Sector of Activity": "Electricite industrielle, construction, genie civil, construction metallique et plomberie",
      "Address": "Hay saada 4 rue 45 n6 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Eolienne (ste d'ingenierie)",
      "Sector of Activity": "Ingenierie, etudes techniques",
      "Address": "7 rue de mexique - Tanger-Assilah"
    },
    {
      "Company Name": "Achhab binaa (ste)",
      "Sector of Activity": "Construction et promotion immobiliere",
      "Address": "5 rue l'hopital espagnol n9 - Tanger-Assilah"
    },
    {
      "Company Name": "Schengen tex (ste)",
      "Sector of Activity": "Confection des vetements et tous articles de pret-a-porter",
      "Address": "Rue khansae n18 castilla - Tanger-Assilah"
    },
    {
      "Company Name": "Boutaour",
      "Sector of Activity": "Import export",
      "Address": "1 rue el moutanabi - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Boughaz (informatique conceptions systeme) (ICSB)",
      "Sector of Activity": "Commerce de prestation en informatique",
      "Address": "7 rue khalid ibn el oualid n12 - Tanger-Assilah"
    },
    {
      "Company Name": "Sorenav",
      "Sector of Activity": "Approvisionnement, ravitaillement, nettoyage des navires",
      "Address": "Rue marseille, résidence la madrague n° 4 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Lyon vannes et raccords-maroc (ste)",
      "Sector of Activity": "Toutes operations commerciales, industrielles, financieres, mobilieres ou immobilieres, susceptibles de favoriser son essor et son developpement",
      "Address": "Parc industriel n3 oukacha - Casablanca"
    },
    {
      "Company Name": "Detroit (chantier du)",
      "Sector of Activity": "Ese de construction et travaux publics",
      "Address": "Florensia tranche 2 rue irak n 6 - Tanger-Assilah"
    },
    {
      "Company Name": "Electro construction industrielle le but (ECIB)",
      "Sector of Activity": "Electricite industrielle, construction, genie civil, construction metallique et plomberie",
      "Address": "Hay saada 4 rue 45 n6 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Eolienne (ste d'ingenierie)",
      "Sector of Activity": "Ingenierie, etudes techniques",
      "Address": "7 rue de mexique - Tanger-Assilah"
    },
    {
      "Company Name": "Achhab binaa (ste)",
      "Sector of Activity": "Construction et promotion immobiliere",
      "Address": "5 rue l'hopital espagnol n9 - Tanger-Assilah"
    },
    {
      "Company Name": "Schengen tex (ste)",
      "Sector of Activity": "Confection des vetements et tous articles de pret-a-porter",
      "Address": "Rue khansae n18 castilla - Tanger-Assilah"
    },
    {
      "Company Name": "Boutaour",
      "Sector of Activity": "Import export",
      "Address": "1 rue el moutanabi - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Boughaz (informatique conceptions systeme) (ICSB)",
      "Sector of Activity": "Commerce de prestation en informatique",
      "Address": "7 rue khalid ibn el oualid n12 - Tanger-Assilah"
    },
    {
      "Company Name": "Sorenav",
      "Sector of Activity": "Approvisionnement, ravitaillement, nettoyage des navires",
      "Address": "Rue marseille, résidence la madrague n° 4 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Lyon vannes et raccords-maroc (ste)",
      "Sector of Activity": "Toutes operations commerciales, industrielles, financieres, mobilieres ou immobilieres, susceptibles de favoriser son essor et son developpement",
      "Address": "Parc industriel n3 oukacha - Casablanca"
    },
    {
      "Company Name": "Laguna auto (ste)",
      "Sector of Activity": "Marchand importateur, marchand de pieces detachees pour voitures automobiles",
      "Address": "9 rue karatchi - Casablanca"
    },
    {
      "Company Name": "Electro construction industrielle le but (ECIB)",
      "Sector of Activity": "Electricite industrielle, construction, genie civil, construction metallique et plomberie",
      "Address": "Hay saada 4 rue 45 n6 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Eolienne (ste d'ingenierie)",
      "Sector of Activity": "Ingenierie, etudes techniques",
      "Address": "7 rue de mexique - Tanger-Assilah"
    },
    {
      "Company Name": "Achhab binaa (ste)",
      "Sector of Activity": "Construction et promotion immobiliere",
      "Address": "5 rue l'hopital espagnol n9 - Tanger-Assilah"
    },
    {
      "Company Name": "Schengen tex (ste)",
      "Sector of Activity": "Confection des vetements et tous articles de pret-a-porter",
      "Address": "Rue khansae n18 castilla - Tanger-Assilah"
    },
    {
      "Company Name": "Boutaour",
      "Sector of Activity": "Import export",
      "Address": "1 rue el moutanabi - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Boughaz (informatique conceptions systeme) (ICSB)",
      "Sector of Activity": "Commerce de prestation en informatique",
      "Address": "7 rue khalid ibn el oualid n12 - Tanger-Assilah"
    },
    {
      "Company Name": "Sorenav",
      "Sector of Activity": "Approvisionnement, ravitaillement, nettoyage des navires",
      "Address": "Rue marseille, résidence la madrague n° 4 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Lyon vannes et raccords-maroc (ste)",
      "Sector of Activity": "Toutes operations commerciales, industrielles, financieres, mobilieres ou immobilieres, susceptibles de favoriser son essor et son developpement",
      "Address": "Parc industriel n3 oukacha - Casablanca"
    },
    {
      "Company Name": "Laguna auto (ste)",
      "Sector of Activity": "Marchand importateur, marchand de pieces detachees pour voitures automobiles",
      "Address": "9 rue karatchi - Casablanca"
    },
    {
      "Company Name": "Socotev (ste) (SOCOTEV)",
      "Sector of Activity": "Controle technique des vihecules automobiles",
      "Address": "31 rue france ville - Casablanca"
    },
    {
      "Company Name": "Eolienne (ste d'ingenierie)",
      "Sector of Activity": "Ingenierie, etudes techniques",
      "Address": "7 rue de mexique - Tanger-Assilah"
    },
    {
      "Company Name": "Achhab binaa (ste)",
      "Sector of Activity": "Construction et promotion immobiliere",
      "Address": "5 rue l'hopital espagnol n9 - Tanger-Assilah"
    },
    {
      "Company Name": "Schengen tex (ste)",
      "Sector of Activity": "Confection des vetements et tous articles de pret-a-porter",
      "Address": "Rue khansae n18 castilla - Tanger-Assilah"
    },
    {
      "Company Name": "Boutaour",
      "Sector of Activity": "Import export",
      "Address": "1 rue el moutanabi - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Boughaz (informatique conceptions systeme) (ICSB)",
      "Sector of Activity": "Commerce de prestation en informatique",
      "Address": "7 rue khalid ibn el oualid n12 - Tanger-Assilah"
    },
    {
      "Company Name": "Sorenav",
      "Sector of Activity": "Approvisionnement, ravitaillement, nettoyage des navires",
      "Address": "Rue marseille, résidence la madrague n° 4 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Lyon vannes et raccords-maroc (ste)",
      "Sector of Activity": "Toutes operations commerciales, industrielles, financieres, mobilieres ou immobilieres, susceptibles de favoriser son essor et son developpement",
      "Address": "Parc industriel n3 oukacha - Casablanca"
    },
    {
      "Company Name": "Laguna auto (ste)",
      "Sector of Activity": "Marchand importateur, marchand de pieces detachees pour voitures automobiles",
      "Address": "9 rue karatchi - Casablanca"
    },
    {
      "Company Name": "Socotev (ste) (SOCOTEV)",
      "Sector of Activity": "Controle technique des vihecules automobiles",
      "Address": "31 rue france ville - Casablanca"
    },
    {
      "Company Name": "Contratas maritimas",
      "Sector of Activity": "Bureau de liaison",
      "Address": "213 bd de la resistance imm yousra 2eme etage n5 - Casablanca"
    },
    {
      "Company Name": "Achhab binaa (ste)",
      "Sector of Activity": "Construction et promotion immobiliere",
      "Address": "5 rue l'hopital espagnol n9 - Tanger-Assilah"
    },
    {
      "Company Name": "Schengen tex (ste)",
      "Sector of Activity": "Confection des vetements et tous articles de pret-a-porter",
      "Address": "Rue khansae n18 castilla - Tanger-Assilah"
    },
    {
      "Company Name": "Boutaour",
      "Sector of Activity": "Import export",
      "Address": "1 rue el moutanabi - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Boughaz (informatique conceptions systeme) (ICSB)",
      "Sector of Activity": "Commerce de prestation en informatique",
      "Address": "7 rue khalid ibn el oualid n12 - Tanger-Assilah"
    },
    {
      "Company Name": "Sorenav",
      "Sector of Activity": "Approvisionnement, ravitaillement, nettoyage des navires",
      "Address": "Rue marseille, résidence la madrague n° 4 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Lyon vannes et raccords-maroc (ste)",
      "Sector of Activity": "Toutes operations commerciales, industrielles, financieres, mobilieres ou immobilieres, susceptibles de favoriser son essor et son developpement",
      "Address": "Parc industriel n3 oukacha - Casablanca"
    },
    {
      "Company Name": "Laguna auto (ste)",
      "Sector of Activity": "Marchand importateur, marchand de pieces detachees pour voitures automobiles",
      "Address": "9 rue karatchi - Casablanca"
    },
    {
      "Company Name": "Socotev (ste) (SOCOTEV)",
      "Sector of Activity": "Controle technique des vihecules automobiles",
      "Address": "31 rue france ville - Casablanca"
    },
    {
      "Company Name": "Contratas maritimas",
      "Sector of Activity": "Bureau de liaison",
      "Address": "213 bd de la resistance imm yousra 2eme etage n5 - Casablanca"
    },
    {
      "Company Name": "Haddioui de developpement d'elevage (ste) (SHDE)",
      "Sector of Activity": "L'elevage et l'agriculture",
      "Address": "30 rue leon l'africain - Casablanca"
    },
    {
      "Company Name": "Schengen tex (ste)",
      "Sector of Activity": "Confection des vetements et tous articles de pret-a-porter",
      "Address": "Rue khansae n18 castilla - Tanger-Assilah"
    },
    {
      "Company Name": "Boutaour",
      "Sector of Activity": "Import export",
      "Address": "1 rue el moutanabi - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Boughaz (informatique conceptions systeme) (ICSB)",
      "Sector of Activity": "Commerce de prestation en informatique",
      "Address": "7 rue khalid ibn el oualid n12 - Tanger-Assilah"
    },
    {
      "Company Name": "Sorenav",
      "Sector of Activity": "Approvisionnement, ravitaillement, nettoyage des navires",
      "Address": "Rue marseille, résidence la madrague n° 4 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Lyon vannes et raccords-maroc (ste)",
      "Sector of Activity": "Toutes operations commerciales, industrielles, financieres, mobilieres ou immobilieres, susceptibles de favoriser son essor et son developpement",
      "Address": "Parc industriel n3 oukacha - Casablanca"
    },
    {
      "Company Name": "Laguna auto (ste)",
      "Sector of Activity": "Marchand importateur, marchand de pieces detachees pour voitures automobiles",
      "Address": "9 rue karatchi - Casablanca"
    },
    {
      "Company Name": "Socotev (ste) (SOCOTEV)",
      "Sector of Activity": "Controle technique des vihecules automobiles",
      "Address": "31 rue france ville - Casablanca"
    },
    {
      "Company Name": "Contratas maritimas",
      "Sector of Activity": "Bureau de liaison",
      "Address": "213 bd de la resistance imm yousra 2eme etage n5 - Casablanca"
    },
    {
      "Company Name": "Haddioui de developpement d'elevage (ste) (SHDE)",
      "Sector of Activity": "L'elevage et l'agriculture",
      "Address": "30 rue leon l'africain - Casablanca"
    },
    {
      "Company Name": "Fox metal (ste)",
      "Sector of Activity": "Travaux de tour et du fraisage du metal",
      "Address": "Bd oum rabie rue 50 n2 el oulfa - Casablanca"
    },
    {
      "Company Name": "Boutaour",
      "Sector of Activity": "Import export",
      "Address": "1 rue el moutanabi - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Boughaz (informatique conceptions systeme) (ICSB)",
      "Sector of Activity": "Commerce de prestation en informatique",
      "Address": "7 rue khalid ibn el oualid n12 - Tanger-Assilah"
    },
    {
      "Company Name": "Sorenav",
      "Sector of Activity": "Approvisionnement, ravitaillement, nettoyage des navires",
      "Address": "Rue marseille, résidence la madrague n° 4 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Lyon vannes et raccords-maroc (ste)",
      "Sector of Activity": "Toutes operations commerciales, industrielles, financieres, mobilieres ou immobilieres, susceptibles de favoriser son essor et son developpement",
      "Address": "Parc industriel n3 oukacha - Casablanca"
    },
    {
      "Company Name": "Laguna auto (ste)",
      "Sector of Activity": "Marchand importateur, marchand de pieces detachees pour voitures automobiles",
      "Address": "9 rue karatchi - Casablanca"
    },
    {
      "Company Name": "Socotev (ste) (SOCOTEV)",
      "Sector of Activity": "Controle technique des vihecules automobiles",
      "Address": "31 rue france ville - Casablanca"
    },
    {
      "Company Name": "Contratas maritimas",
      "Sector of Activity": "Bureau de liaison",
      "Address": "213 bd de la resistance imm yousra 2eme etage n5 - Casablanca"
    },
    {
      "Company Name": "Haddioui de developpement d'elevage (ste) (SHDE)",
      "Sector of Activity": "L'elevage et l'agriculture",
      "Address": "30 rue leon l'africain - Casablanca"
    },
    {
      "Company Name": "Fox metal (ste)",
      "Sector of Activity": "Travaux de tour et du fraisage du metal",
      "Address": "Bd oum rabie rue 50 n2 el oulfa - Casablanca"
    },
    {
      "Company Name": "L.b.s fisheries",
      "Sector of Activity": "Import export congelation et traitement des produits de mers et agricole congelation des poissons",
      "Address": "Lot 63 nouveau port - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Boughaz (informatique conceptions systeme) (ICSB)",
      "Sector of Activity": "Commerce de prestation en informatique",
      "Address": "7 rue khalid ibn el oualid n12 - Tanger-Assilah"
    },
    {
      "Company Name": "Sorenav",
      "Sector of Activity": "Approvisionnement, ravitaillement, nettoyage des navires",
      "Address": "Rue marseille, résidence la madrague n° 4 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Lyon vannes et raccords-maroc (ste)",
      "Sector of Activity": "Toutes operations commerciales, industrielles, financieres, mobilieres ou immobilieres, susceptibles de favoriser son essor et son developpement",
      "Address": "Parc industriel n3 oukacha - Casablanca"
    },
    {
      "Company Name": "Laguna auto (ste)",
      "Sector of Activity": "Marchand importateur, marchand de pieces detachees pour voitures automobiles",
      "Address": "9 rue karatchi - Casablanca"
    },
    {
      "Company Name": "Socotev (ste) (SOCOTEV)",
      "Sector of Activity": "Controle technique des vihecules automobiles",
      "Address": "31 rue france ville - Casablanca"
    },
    {
      "Company Name": "Contratas maritimas",
      "Sector of Activity": "Bureau de liaison",
      "Address": "213 bd de la resistance imm yousra 2eme etage n5 - Casablanca"
    },
    {
      "Company Name": "Haddioui de developpement d'elevage (ste) (SHDE)",
      "Sector of Activity": "L'elevage et l'agriculture",
      "Address": "30 rue leon l'africain - Casablanca"
    },
    {
      "Company Name": "Fox metal (ste)",
      "Sector of Activity": "Travaux de tour et du fraisage du metal",
      "Address": "Bd oum rabie rue 50 n2 el oulfa - Casablanca"
    },
    {
      "Company Name": "L.b.s fisheries",
      "Sector of Activity": "Import export congelation et traitement des produits de mers et agricole congelation des poissons",
      "Address": "Lot 63 nouveau port - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Martil bois",
      "Sector of Activity": "Commercialisation de bois/import-export - vente en detail et en gros de bois",
      "Address": "Douar oulad said m'hamed jakma - Berrechid (M)"
    },
    {
      "Company Name": "Sorenav",
      "Sector of Activity": "Approvisionnement, ravitaillement, nettoyage des navires",
      "Address": "Rue marseille, résidence la madrague n° 4 - Tanger-Médina (AR)"
    },
    {
      "Company Name": "Lyon vannes et raccords-maroc (ste)",
      "Sector of Activity": "Toutes operations commerciales, industrielles, financieres, mobilieres ou immobilieres, susceptibles de favoriser son essor et son developpement",
      "Address": "Parc industriel n3 oukacha - Casablanca"
    },
    {
      "Company Name": "Laguna auto (ste)",
      "Sector of Activity": "Marchand importateur, marchand de pieces detachees pour voitures automobiles",
      "Address": "9 rue karatchi - Casablanca"
    },
    {
      "Company Name": "Socotev (ste) (SOCOTEV)",
      "Sector of Activity": "Controle technique des vihecules automobiles",
      "Address": "31 rue france ville - Casablanca"
    },
    {
      "Company Name": "Contratas maritimas",
      "Sector of Activity": "Bureau de liaison",
      "Address": "213 bd de la resistance imm yousra 2eme etage n5 - Casablanca"
    },
    {
      "Company Name": "Haddioui de developpement d'elevage (ste) (SHDE)",
      "Sector of Activity": "L'elevage et l'agriculture",
      "Address": "30 rue leon l'africain - Casablanca"
    },
    {
      "Company Name": "Fox metal (ste)",
      "Sector of Activity": "Travaux de tour et du fraisage du metal",
      "Address": "Bd oum rabie rue 50 n2 el oulfa - Casablanca"
    },
    {
      "Company Name": "L.b.s fisheries",
      "Sector of Activity": "Import export congelation et traitement des produits de mers et agricole congelation des poissons",
      "Address": "Lot 63 nouveau port - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Martil bois",
      "Sector of Activity": "Commercialisation de bois/import-export - vente en detail et en gros de bois",
      "Address": "Douar oulad said m'hamed jakma - Berrechid (M)"
    },
    {
      "Company Name": "Bikhir car",
      "Sector of Activity": "Location de vehicules automobiles sans chauffeur",
      "Address": "N?37 rue drarga - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Lyon vannes et raccords-maroc (ste)",
      "Sector of Activity": "Toutes operations commerciales, industrielles, financieres, mobilieres ou immobilieres, susceptibles de favoriser son essor et son developpement",
      "Address": "Parc industriel n3 oukacha - Casablanca"
    },
    {
      "Company Name": "Laguna auto (ste)",
      "Sector of Activity": "Marchand importateur, marchand de pieces detachees pour voitures automobiles",
      "Address": "9 rue karatchi - Casablanca"
    },
    {
      "Company Name": "Socotev (ste) (SOCOTEV)",
      "Sector of Activity": "Controle technique des vihecules automobiles",
      "Address": "31 rue france ville - Casablanca"
    },
    {
      "Company Name": "Contratas maritimas",
      "Sector of Activity": "Bureau de liaison",
      "Address": "213 bd de la resistance imm yousra 2eme etage n5 - Casablanca"
    },
    {
      "Company Name": "Haddioui de developpement d'elevage (ste) (SHDE)",
      "Sector of Activity": "L'elevage et l'agriculture",
      "Address": "30 rue leon l'africain - Casablanca"
    },
    {
      "Company Name": "Fox metal (ste)",
      "Sector of Activity": "Travaux de tour et du fraisage du metal",
      "Address": "Bd oum rabie rue 50 n2 el oulfa - Casablanca"
    },
    {
      "Company Name": "L.b.s fisheries",
      "Sector of Activity": "Import export congelation et traitement des produits de mers et agricole congelation des poissons",
      "Address": "Lot 63 nouveau port - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Martil bois",
      "Sector of Activity": "Commercialisation de bois/import-export - vente en detail et en gros de bois",
      "Address": "Douar oulad said m'hamed jakma - Berrechid (M)"
    },
    {
      "Company Name": "Bikhir car",
      "Sector of Activity": "Location de vehicules automobiles sans chauffeur",
      "Address": "N?37 rue drarga - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "La foire aux affaires france - maroc",
      "Sector of Activity": "Import export en general",
      "Address": "72 lot founty sonaba - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Laguna auto (ste)",
      "Sector of Activity": "Marchand importateur, marchand de pieces detachees pour voitures automobiles",
      "Address": "9 rue karatchi - Casablanca"
    },
    {
      "Company Name": "Socotev (ste) (SOCOTEV)",
      "Sector of Activity": "Controle technique des vihecules automobiles",
      "Address": "31 rue france ville - Casablanca"
    },
    {
      "Company Name": "Contratas maritimas",
      "Sector of Activity": "Bureau de liaison",
      "Address": "213 bd de la resistance imm yousra 2eme etage n5 - Casablanca"
    },
    {
      "Company Name": "Haddioui de developpement d'elevage (ste) (SHDE)",
      "Sector of Activity": "L'elevage et l'agriculture",
      "Address": "30 rue leon l'africain - Casablanca"
    },
    {
      "Company Name": "Fox metal (ste)",
      "Sector of Activity": "Travaux de tour et du fraisage du metal",
      "Address": "Bd oum rabie rue 50 n2 el oulfa - Casablanca"
    },
    {
      "Company Name": "L.b.s fisheries",
      "Sector of Activity": "Import export congelation et traitement des produits de mers et agricole congelation des poissons",
      "Address": "Lot 63 nouveau port - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Martil bois",
      "Sector of Activity": "Commercialisation de bois/import-export - vente en detail et en gros de bois",
      "Address": "Douar oulad said m'hamed jakma - Berrechid (M)"
    },
    {
      "Company Name": "Bikhir car",
      "Sector of Activity": "Location de vehicules automobiles sans chauffeur",
      "Address": "N?37 rue drarga - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "La foire aux affaires france - maroc",
      "Sector of Activity": "Import export en general",
      "Address": "72 lot founty sonaba - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Assalaf chaabi pour le sud",
      "Sector of Activity": "Operation de financement et de credit",
      "Address": "Lotissement faiz, rue 204 n 7 quartier industriel - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Socotev (ste) (SOCOTEV)",
      "Sector of Activity": "Controle technique des vihecules automobiles",
      "Address": "31 rue france ville - Casablanca"
    },
    {
      "Company Name": "Contratas maritimas",
      "Sector of Activity": "Bureau de liaison",
      "Address": "213 bd de la resistance imm yousra 2eme etage n5 - Casablanca"
    },
    {
      "Company Name": "Haddioui de developpement d'elevage (ste) (SHDE)",
      "Sector of Activity": "L'elevage et l'agriculture",
      "Address": "30 rue leon l'africain - Casablanca"
    },
    {
      "Company Name": "Fox metal (ste)",
      "Sector of Activity": "Travaux de tour et du fraisage du metal",
      "Address": "Bd oum rabie rue 50 n2 el oulfa - Casablanca"
    },
    {
      "Company Name": "L.b.s fisheries",
      "Sector of Activity": "Import export congelation et traitement des produits de mers et agricole congelation des poissons",
      "Address": "Lot 63 nouveau port - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Martil bois",
      "Sector of Activity": "Commercialisation de bois/import-export - vente en detail et en gros de bois",
      "Address": "Douar oulad said m'hamed jakma - Berrechid (M)"
    },
    {
      "Company Name": "Bikhir car",
      "Sector of Activity": "Location de vehicules automobiles sans chauffeur",
      "Address": "N?37 rue drarga - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "La foire aux affaires france - maroc",
      "Sector of Activity": "Import export en general",
      "Address": "72 lot founty sonaba - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Assalaf chaabi pour le sud",
      "Sector of Activity": "Operation de financement et de credit",
      "Address": "Lotissement faiz, rue 204 n 7 quartier industriel - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Cohismar transit",
      "Sector of Activity": "Transitaire - marchand effectuant importation exportation",
      "Address": "Imm. hasana av. hassan ii - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Contratas maritimas",
      "Sector of Activity": "Bureau de liaison",
      "Address": "213 bd de la resistance imm yousra 2eme etage n5 - Casablanca"
    },
    {
      "Company Name": "Haddioui de developpement d'elevage (ste) (SHDE)",
      "Sector of Activity": "L'elevage et l'agriculture",
      "Address": "30 rue leon l'africain - Casablanca"
    },
    {
      "Company Name": "Fox metal (ste)",
      "Sector of Activity": "Travaux de tour et du fraisage du metal",
      "Address": "Bd oum rabie rue 50 n2 el oulfa - Casablanca"
    },
    {
      "Company Name": "L.b.s fisheries",
      "Sector of Activity": "Import export congelation et traitement des produits de mers et agricole congelation des poissons",
      "Address": "Lot 63 nouveau port - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Martil bois",
      "Sector of Activity": "Commercialisation de bois/import-export - vente en detail et en gros de bois",
      "Address": "Douar oulad said m'hamed jakma - Berrechid (M)"
    },
    {
      "Company Name": "Bikhir car",
      "Sector of Activity": "Location de vehicules automobiles sans chauffeur",
      "Address": "N?37 rue drarga - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "La foire aux affaires france - maroc",
      "Sector of Activity": "Import export en general",
      "Address": "72 lot founty sonaba - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Assalaf chaabi pour le sud",
      "Sector of Activity": "Operation de financement et de credit",
      "Address": "Lotissement faiz, rue 204 n 7 quartier industriel - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Cohismar transit",
      "Sector of Activity": "Transitaire - marchand effectuant importation exportation",
      "Address": "Imm. hasana av. hassan ii - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Convabene",
      "Sector of Activity": "Fabricant de vetements confectionnes-md effectuant import export",
      "Address": "5 rue ibnou laknane ain sebaa - Aîn-Sebaâ (AR)"
    },
    {
      "Company Name": "Haddioui de developpement d'elevage (ste) (SHDE)",
      "Sector of Activity": "L'elevage et l'agriculture",
      "Address": "30 rue leon l'africain - Casablanca"
    },
    {
      "Company Name": "Fox metal (ste)",
      "Sector of Activity": "Travaux de tour et du fraisage du metal",
      "Address": "Bd oum rabie rue 50 n2 el oulfa - Casablanca"
    },
    {
      "Company Name": "L.b.s fisheries",
      "Sector of Activity": "Import export congelation et traitement des produits de mers et agricole congelation des poissons",
      "Address": "Lot 63 nouveau port - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Martil bois",
      "Sector of Activity": "Commercialisation de bois/import-export - vente en detail et en gros de bois",
      "Address": "Douar oulad said m'hamed jakma - Berrechid (M)"
    },
    {
      "Company Name": "Bikhir car",
      "Sector of Activity": "Location de vehicules automobiles sans chauffeur",
      "Address": "N?37 rue drarga - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "La foire aux affaires france - maroc",
      "Sector of Activity": "Import export en general",
      "Address": "72 lot founty sonaba - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Assalaf chaabi pour le sud",
      "Sector of Activity": "Operation de financement et de credit",
      "Address": "Lotissement faiz, rue 204 n 7 quartier industriel - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Cohismar transit",
      "Sector of Activity": "Transitaire - marchand effectuant importation exportation",
      "Address": "Imm. hasana av. hassan ii - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Convabene",
      "Sector of Activity": "Fabricant de vetements confectionnes-md effectuant import export",
      "Address": "5 rue ibnou laknane ain sebaa - Aîn-Sebaâ (AR)"
    },
    {
      "Company Name": "Societe bougaccafe",
      "Sector of Activity": "Terrefication du cafe",
      "Address": "12 rue omar khiamcite mly. rachid - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Fox metal (ste)",
      "Sector of Activity": "Travaux de tour et du fraisage du metal",
      "Address": "Bd oum rabie rue 50 n2 el oulfa - Casablanca"
    },
    {
      "Company Name": "L.b.s fisheries",
      "Sector of Activity": "Import export congelation et traitement des produits de mers et agricole congelation des poissons",
      "Address": "Lot 63 nouveau port - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Martil bois",
      "Sector of Activity": "Commercialisation de bois/import-export - vente en detail et en gros de bois",
      "Address": "Douar oulad said m'hamed jakma - Berrechid (M)"
    },
    {
      "Company Name": "Bikhir car",
      "Sector of Activity": "Location de vehicules automobiles sans chauffeur",
      "Address": "N?37 rue drarga - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "La foire aux affaires france - maroc",
      "Sector of Activity": "Import export en general",
      "Address": "72 lot founty sonaba - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Assalaf chaabi pour le sud",
      "Sector of Activity": "Operation de financement et de credit",
      "Address": "Lotissement faiz, rue 204 n 7 quartier industriel - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Cohismar transit",
      "Sector of Activity": "Transitaire - marchand effectuant importation exportation",
      "Address": "Imm. hasana av. hassan ii - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Convabene",
      "Sector of Activity": "Fabricant de vetements confectionnes-md effectuant import export",
      "Address": "5 rue ibnou laknane ain sebaa - Aîn-Sebaâ (AR)"
    },
    {
      "Company Name": "Societe bougaccafe",
      "Sector of Activity": "Terrefication du cafe",
      "Address": "12 rue omar khiamcite mly. rachid - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Groupe repro",
      "Sector of Activity": "- reprographie, impression numérique et offset",
      "Address": "7 rdc rue nassiheddine - ex eglantines, maârif - El Maarif (AR)"
    },
    {
      "Company Name": "L.b.s fisheries",
      "Sector of Activity": "Import export congelation et traitement des produits de mers et agricole congelation des poissons",
      "Address": "Lot 63 nouveau port - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Martil bois",
      "Sector of Activity": "Commercialisation de bois/import-export - vente en detail et en gros de bois",
      "Address": "Douar oulad said m'hamed jakma - Berrechid (M)"
    },
    {
      "Company Name": "Bikhir car",
      "Sector of Activity": "Location de vehicules automobiles sans chauffeur",
      "Address": "N?37 rue drarga - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "La foire aux affaires france - maroc",
      "Sector of Activity": "Import export en general",
      "Address": "72 lot founty sonaba - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Assalaf chaabi pour le sud",
      "Sector of Activity": "Operation de financement et de credit",
      "Address": "Lotissement faiz, rue 204 n 7 quartier industriel - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Cohismar transit",
      "Sector of Activity": "Transitaire - marchand effectuant importation exportation",
      "Address": "Imm. hasana av. hassan ii - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Convabene",
      "Sector of Activity": "Fabricant de vetements confectionnes-md effectuant import export",
      "Address": "5 rue ibnou laknane ain sebaa - Aîn-Sebaâ (AR)"
    },
    {
      "Company Name": "Societe bougaccafe",
      "Sector of Activity": "Terrefication du cafe",
      "Address": "12 rue omar khiamcite mly. rachid - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Groupe repro",
      "Sector of Activity": "- reprographie, impression numérique et offset",
      "Address": "7 rdc rue nassiheddine - ex eglantines, maârif - El Maarif (AR)"
    },
    {
      "Company Name": "Igrane vert",
      "Sector of Activity": "Tenant un bureau d'etudes, etudes des espaces verts et reboisement, entrepreneur de travaux divers et effet import export - négociant en tout genre de produits. - réalisation des saguias et ouvertures des pistes. - toutes transactions d'achats, ventes et location mobilière et immobilière. - promotion immobilière. - import et export produits artisanats.",
      "Address": "Rue rabat n4 port laayoune - Laayoune (M)"
    },
    {
      "Company Name": "Martil bois",
      "Sector of Activity": "Commercialisation de bois/import-export - vente en detail et en gros de bois",
      "Address": "Douar oulad said m'hamed jakma - Berrechid (M)"
    },
    {
      "Company Name": "Bikhir car",
      "Sector of Activity": "Location de vehicules automobiles sans chauffeur",
      "Address": "N?37 rue drarga - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "La foire aux affaires france - maroc",
      "Sector of Activity": "Import export en general",
      "Address": "72 lot founty sonaba - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Assalaf chaabi pour le sud",
      "Sector of Activity": "Operation de financement et de credit",
      "Address": "Lotissement faiz, rue 204 n 7 quartier industriel - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Cohismar transit",
      "Sector of Activity": "Transitaire - marchand effectuant importation exportation",
      "Address": "Imm. hasana av. hassan ii - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Convabene",
      "Sector of Activity": "Fabricant de vetements confectionnes-md effectuant import export",
      "Address": "5 rue ibnou laknane ain sebaa - Aîn-Sebaâ (AR)"
    },
    {
      "Company Name": "Societe bougaccafe",
      "Sector of Activity": "Terrefication du cafe",
      "Address": "12 rue omar khiamcite mly. rachid - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Groupe repro",
      "Sector of Activity": "- reprographie, impression numérique et offset",
      "Address": "7 rdc rue nassiheddine - ex eglantines, maârif - El Maarif (AR)"
    },
    {
      "Company Name": "Igrane vert",
      "Sector of Activity": "Tenant un bureau d'etudes, etudes des espaces verts et reboisement, entrepreneur de travaux divers et effet import export - négociant en tout genre de produits. - réalisation des saguias et ouvertures des pistes. - toutes transactions d'achats, ventes et location mobilière et immobilière. - promotion immobilière. - import et export produits artisanats.",
      "Address": "Rue rabat n4 port laayoune - Laayoune (M)"
    },
    {
      "Company Name": "Univers fiscalite et analyse comptable (UNIFAC)",
      "Sector of Activity": "Service de traitement fiscale et comptable",
      "Address": "N?67 av. hassan 1 cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Bikhir car",
      "Sector of Activity": "Location de vehicules automobiles sans chauffeur",
      "Address": "N?37 rue drarga - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "La foire aux affaires france - maroc",
      "Sector of Activity": "Import export en general",
      "Address": "72 lot founty sonaba - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Assalaf chaabi pour le sud",
      "Sector of Activity": "Operation de financement et de credit",
      "Address": "Lotissement faiz, rue 204 n 7 quartier industriel - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Cohismar transit",
      "Sector of Activity": "Transitaire - marchand effectuant importation exportation",
      "Address": "Imm. hasana av. hassan ii - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Convabene",
      "Sector of Activity": "Fabricant de vetements confectionnes-md effectuant import export",
      "Address": "5 rue ibnou laknane ain sebaa - Aîn-Sebaâ (AR)"
    },
    {
      "Company Name": "Societe bougaccafe",
      "Sector of Activity": "Terrefication du cafe",
      "Address": "12 rue omar khiamcite mly. rachid - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Groupe repro",
      "Sector of Activity": "- reprographie, impression numérique et offset",
      "Address": "7 rdc rue nassiheddine - ex eglantines, maârif - El Maarif (AR)"
    },
    {
      "Company Name": "Igrane vert",
      "Sector of Activity": "Tenant un bureau d'etudes, etudes des espaces verts et reboisement, entrepreneur de travaux divers et effet import export - négociant en tout genre de produits. - réalisation des saguias et ouvertures des pistes. - toutes transactions d'achats, ventes et location mobilière et immobilière. - promotion immobilière. - import et export produits artisanats.",
      "Address": "Rue rabat n4 port laayoune - Laayoune (M)"
    },
    {
      "Company Name": "Univers fiscalite et analyse comptable (UNIFAC)",
      "Sector of Activity": "Service de traitement fiscale et comptable",
      "Address": "N?67 av. hassan 1 cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Point sud",
      "Sector of Activity": "Agence de voyage tourisme",
      "Address": "Complexe anzi n?4 bd. mohamed v - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "La foire aux affaires france - maroc",
      "Sector of Activity": "Import export en general",
      "Address": "72 lot founty sonaba - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Assalaf chaabi pour le sud",
      "Sector of Activity": "Operation de financement et de credit",
      "Address": "Lotissement faiz, rue 204 n 7 quartier industriel - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Cohismar transit",
      "Sector of Activity": "Transitaire - marchand effectuant importation exportation",
      "Address": "Imm. hasana av. hassan ii - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Convabene",
      "Sector of Activity": "Fabricant de vetements confectionnes-md effectuant import export",
      "Address": "5 rue ibnou laknane ain sebaa - Aîn-Sebaâ (AR)"
    },
    {
      "Company Name": "Societe bougaccafe",
      "Sector of Activity": "Terrefication du cafe",
      "Address": "12 rue omar khiamcite mly. rachid - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Groupe repro",
      "Sector of Activity": "- reprographie, impression numérique et offset",
      "Address": "7 rdc rue nassiheddine - ex eglantines, maârif - El Maarif (AR)"
    },
    {
      "Company Name": "Igrane vert",
      "Sector of Activity": "Tenant un bureau d'etudes, etudes des espaces verts et reboisement, entrepreneur de travaux divers et effet import export - négociant en tout genre de produits. - réalisation des saguias et ouvertures des pistes. - toutes transactions d'achats, ventes et location mobilière et immobilière. - promotion immobilière. - import et export produits artisanats.",
      "Address": "Rue rabat n4 port laayoune - Laayoune (M)"
    },
    {
      "Company Name": "Univers fiscalite et analyse comptable (UNIFAC)",
      "Sector of Activity": "Service de traitement fiscale et comptable",
      "Address": "N?67 av. hassan 1 cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Point sud",
      "Sector of Activity": "Agence de voyage tourisme",
      "Address": "Complexe anzi n?4 bd. mohamed v - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Rimal vacance services (RVS)",
      "Sector of Activity": "Transport touristique",
      "Address": "408, bd mohamed zerktouni, résid. elistikrare, 2°ét. - Casablanca"
    },
    {
      "Company Name": "Assalaf chaabi pour le sud",
      "Sector of Activity": "Operation de financement et de credit",
      "Address": "Lotissement faiz, rue 204 n 7 quartier industriel - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Cohismar transit",
      "Sector of Activity": "Transitaire - marchand effectuant importation exportation",
      "Address": "Imm. hasana av. hassan ii - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Convabene",
      "Sector of Activity": "Fabricant de vetements confectionnes-md effectuant import export",
      "Address": "5 rue ibnou laknane ain sebaa - Aîn-Sebaâ (AR)"
    },
    {
      "Company Name": "Societe bougaccafe",
      "Sector of Activity": "Terrefication du cafe",
      "Address": "12 rue omar khiamcite mly. rachid - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Groupe repro",
      "Sector of Activity": "- reprographie, impression numérique et offset",
      "Address": "7 rdc rue nassiheddine - ex eglantines, maârif - El Maarif (AR)"
    },
    {
      "Company Name": "Igrane vert",
      "Sector of Activity": "Tenant un bureau d'etudes, etudes des espaces verts et reboisement, entrepreneur de travaux divers et effet import export - négociant en tout genre de produits. - réalisation des saguias et ouvertures des pistes. - toutes transactions d'achats, ventes et location mobilière et immobilière. - promotion immobilière. - import et export produits artisanats.",
      "Address": "Rue rabat n4 port laayoune - Laayoune (M)"
    },
    {
      "Company Name": "Univers fiscalite et analyse comptable (UNIFAC)",
      "Sector of Activity": "Service de traitement fiscale et comptable",
      "Address": "N?67 av. hassan 1 cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Point sud",
      "Sector of Activity": "Agence de voyage tourisme",
      "Address": "Complexe anzi n?4 bd. mohamed v - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Rimal vacance services (RVS)",
      "Sector of Activity": "Transport touristique",
      "Address": "408, bd mohamed zerktouni, résid. elistikrare, 2°ét. - Casablanca"
    },
    {
      "Company Name": "Menuiserie ebenisterie france ville",
      "Sector of Activity": "La menuiserie et ebenesterie",
      "Address": "N?37 bd. farhat hachad cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Cohismar transit",
      "Sector of Activity": "Transitaire - marchand effectuant importation exportation",
      "Address": "Imm. hasana av. hassan ii - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Convabene",
      "Sector of Activity": "Fabricant de vetements confectionnes-md effectuant import export",
      "Address": "5 rue ibnou laknane ain sebaa - Aîn-Sebaâ (AR)"
    },
    {
      "Company Name": "Societe bougaccafe",
      "Sector of Activity": "Terrefication du cafe",
      "Address": "12 rue omar khiamcite mly. rachid - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Groupe repro",
      "Sector of Activity": "- reprographie, impression numérique et offset",
      "Address": "7 rdc rue nassiheddine - ex eglantines, maârif - El Maarif (AR)"
    },
    {
      "Company Name": "Igrane vert",
      "Sector of Activity": "Tenant un bureau d'etudes, etudes des espaces verts et reboisement, entrepreneur de travaux divers et effet import export - négociant en tout genre de produits. - réalisation des saguias et ouvertures des pistes. - toutes transactions d'achats, ventes et location mobilière et immobilière. - promotion immobilière. - import et export produits artisanats.",
      "Address": "Rue rabat n4 port laayoune - Laayoune (M)"
    },
    {
      "Company Name": "Univers fiscalite et analyse comptable (UNIFAC)",
      "Sector of Activity": "Service de traitement fiscale et comptable",
      "Address": "N?67 av. hassan 1 cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Point sud",
      "Sector of Activity": "Agence de voyage tourisme",
      "Address": "Complexe anzi n?4 bd. mohamed v - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Rimal vacance services (RVS)",
      "Sector of Activity": "Transport touristique",
      "Address": "408, bd mohamed zerktouni, résid. elistikrare, 2°ét. - Casablanca"
    },
    {
      "Company Name": "Menuiserie ebenisterie france ville",
      "Sector of Activity": "La menuiserie et ebenesterie",
      "Address": "N?37 bd. farhat hachad cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Jardin d'or",
      "Sector of Activity": "- restauration - pizza et chawarma",
      "Address": "27 complexe commercial tawada front de mer - Agadir (M)"
    },
    {
      "Company Name": "Convabene",
      "Sector of Activity": "Fabricant de vetements confectionnes-md effectuant import export",
      "Address": "5 rue ibnou laknane ain sebaa - Aîn-Sebaâ (AR)"
    },
    {
      "Company Name": "Societe bougaccafe",
      "Sector of Activity": "Terrefication du cafe",
      "Address": "12 rue omar khiamcite mly. rachid - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Groupe repro",
      "Sector of Activity": "- reprographie, impression numérique et offset",
      "Address": "7 rdc rue nassiheddine - ex eglantines, maârif - El Maarif (AR)"
    },
    {
      "Company Name": "Igrane vert",
      "Sector of Activity": "Tenant un bureau d'etudes, etudes des espaces verts et reboisement, entrepreneur de travaux divers et effet import export - négociant en tout genre de produits. - réalisation des saguias et ouvertures des pistes. - toutes transactions d'achats, ventes et location mobilière et immobilière. - promotion immobilière. - import et export produits artisanats.",
      "Address": "Rue rabat n4 port laayoune - Laayoune (M)"
    },
    {
      "Company Name": "Univers fiscalite et analyse comptable (UNIFAC)",
      "Sector of Activity": "Service de traitement fiscale et comptable",
      "Address": "N?67 av. hassan 1 cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Point sud",
      "Sector of Activity": "Agence de voyage tourisme",
      "Address": "Complexe anzi n?4 bd. mohamed v - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Rimal vacance services (RVS)",
      "Sector of Activity": "Transport touristique",
      "Address": "408, bd mohamed zerktouni, résid. elistikrare, 2°ét. - Casablanca"
    },
    {
      "Company Name": "Menuiserie ebenisterie france ville",
      "Sector of Activity": "La menuiserie et ebenesterie",
      "Address": "N?37 bd. farhat hachad cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Jardin d'or",
      "Sector of Activity": "- restauration - pizza et chawarma",
      "Address": "27 complexe commercial tawada front de mer - Agadir (M)"
    },
    {
      "Company Name": "Ste ideal editions 2000",
      "Sector of Activity": "- travaux d'imprimerie",
      "Address": "31 bloc 65 sidi othmane - Casablanca"
    },
    {
      "Company Name": "Societe bougaccafe",
      "Sector of Activity": "Terrefication du cafe",
      "Address": "12 rue omar khiamcite mly. rachid - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Groupe repro",
      "Sector of Activity": "- reprographie, impression numérique et offset",
      "Address": "7 rdc rue nassiheddine - ex eglantines, maârif - El Maarif (AR)"
    },
    {
      "Company Name": "Igrane vert",
      "Sector of Activity": "Tenant un bureau d'etudes, etudes des espaces verts et reboisement, entrepreneur de travaux divers et effet import export - négociant en tout genre de produits. - réalisation des saguias et ouvertures des pistes. - toutes transactions d'achats, ventes et location mobilière et immobilière. - promotion immobilière. - import et export produits artisanats.",
      "Address": "Rue rabat n4 port laayoune - Laayoune (M)"
    },
    {
      "Company Name": "Univers fiscalite et analyse comptable (UNIFAC)",
      "Sector of Activity": "Service de traitement fiscale et comptable",
      "Address": "N?67 av. hassan 1 cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Point sud",
      "Sector of Activity": "Agence de voyage tourisme",
      "Address": "Complexe anzi n?4 bd. mohamed v - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Rimal vacance services (RVS)",
      "Sector of Activity": "Transport touristique",
      "Address": "408, bd mohamed zerktouni, résid. elistikrare, 2°ét. - Casablanca"
    },
    {
      "Company Name": "Menuiserie ebenisterie france ville",
      "Sector of Activity": "La menuiserie et ebenesterie",
      "Address": "N?37 bd. farhat hachad cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Jardin d'or",
      "Sector of Activity": "- restauration - pizza et chawarma",
      "Address": "27 complexe commercial tawada front de mer - Agadir (M)"
    },
    {
      "Company Name": "Ste ideal editions 2000",
      "Sector of Activity": "- travaux d'imprimerie",
      "Address": "31 bloc 65 sidi othmane - Casablanca"
    },
    {
      "Company Name": "World park (ste)",
      "Sector of Activity": "Gestion realisations de parks d'attractions",
      "Address": "Av des far 10 eme etage - Casablanca"
    },
    {
      "Company Name": "Groupe repro",
      "Sector of Activity": "- reprographie, impression numérique et offset",
      "Address": "7 rdc rue nassiheddine - ex eglantines, maârif - El Maarif (AR)"
    },
    {
      "Company Name": "Igrane vert",
      "Sector of Activity": "Tenant un bureau d'etudes, etudes des espaces verts et reboisement, entrepreneur de travaux divers et effet import export - négociant en tout genre de produits. - réalisation des saguias et ouvertures des pistes. - toutes transactions d'achats, ventes et location mobilière et immobilière. - promotion immobilière. - import et export produits artisanats.",
      "Address": "Rue rabat n4 port laayoune - Laayoune (M)"
    },
    {
      "Company Name": "Univers fiscalite et analyse comptable (UNIFAC)",
      "Sector of Activity": "Service de traitement fiscale et comptable",
      "Address": "N?67 av. hassan 1 cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Point sud",
      "Sector of Activity": "Agence de voyage tourisme",
      "Address": "Complexe anzi n?4 bd. mohamed v - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Rimal vacance services (RVS)",
      "Sector of Activity": "Transport touristique",
      "Address": "408, bd mohamed zerktouni, résid. elistikrare, 2°ét. - Casablanca"
    },
    {
      "Company Name": "Menuiserie ebenisterie france ville",
      "Sector of Activity": "La menuiserie et ebenesterie",
      "Address": "N?37 bd. farhat hachad cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Jardin d'or",
      "Sector of Activity": "- restauration - pizza et chawarma",
      "Address": "27 complexe commercial tawada front de mer - Agadir (M)"
    },
    {
      "Company Name": "Ste ideal editions 2000",
      "Sector of Activity": "- travaux d'imprimerie",
      "Address": "31 bloc 65 sidi othmane - Casablanca"
    },
    {
      "Company Name": "World park (ste)",
      "Sector of Activity": "Gestion realisations de parks d'attractions",
      "Address": "Av des far 10 eme etage - Casablanca"
    },
    {
      "Company Name": "Diffusion kenzy",
      "Sector of Activity": "Fabricant de vetements confectionnes-md import export",
      "Address": "19 imm - cb rue abou abbès azfi - El Maarif (AR)"
    },
    {
      "Company Name": "Igrane vert",
      "Sector of Activity": "Tenant un bureau d'etudes, etudes des espaces verts et reboisement, entrepreneur de travaux divers et effet import export - négociant en tout genre de produits. - réalisation des saguias et ouvertures des pistes. - toutes transactions d'achats, ventes et location mobilière et immobilière. - promotion immobilière. - import et export produits artisanats.",
      "Address": "Rue rabat n4 port laayoune - Laayoune (M)"
    },
    {
      "Company Name": "Univers fiscalite et analyse comptable (UNIFAC)",
      "Sector of Activity": "Service de traitement fiscale et comptable",
      "Address": "N?67 av. hassan 1 cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Point sud",
      "Sector of Activity": "Agence de voyage tourisme",
      "Address": "Complexe anzi n?4 bd. mohamed v - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Rimal vacance services (RVS)",
      "Sector of Activity": "Transport touristique",
      "Address": "408, bd mohamed zerktouni, résid. elistikrare, 2°ét. - Casablanca"
    },
    {
      "Company Name": "Menuiserie ebenisterie france ville",
      "Sector of Activity": "La menuiserie et ebenesterie",
      "Address": "N?37 bd. farhat hachad cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Jardin d'or",
      "Sector of Activity": "- restauration - pizza et chawarma",
      "Address": "27 complexe commercial tawada front de mer - Agadir (M)"
    },
    {
      "Company Name": "Ste ideal editions 2000",
      "Sector of Activity": "- travaux d'imprimerie",
      "Address": "31 bloc 65 sidi othmane - Casablanca"
    },
    {
      "Company Name": "World park (ste)",
      "Sector of Activity": "Gestion realisations de parks d'attractions",
      "Address": "Av des far 10 eme etage - Casablanca"
    },
    {
      "Company Name": "Diffusion kenzy",
      "Sector of Activity": "Fabricant de vetements confectionnes-md import export",
      "Address": "19 imm - cb rue abou abbès azfi - El Maarif (AR)"
    },
    {
      "Company Name": "Majestic hotels limited (ste)",
      "Sector of Activity": "Societe hoteliere",
      "Address": "Hotel amphitrite - Skhirate- Temara"
    },
    {
      "Company Name": "Univers fiscalite et analyse comptable (UNIFAC)",
      "Sector of Activity": "Service de traitement fiscale et comptable",
      "Address": "N?67 av. hassan 1 cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Point sud",
      "Sector of Activity": "Agence de voyage tourisme",
      "Address": "Complexe anzi n?4 bd. mohamed v - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Rimal vacance services (RVS)",
      "Sector of Activity": "Transport touristique",
      "Address": "408, bd mohamed zerktouni, résid. elistikrare, 2°ét. - Casablanca"
    },
    {
      "Company Name": "Menuiserie ebenisterie france ville",
      "Sector of Activity": "La menuiserie et ebenesterie",
      "Address": "N?37 bd. farhat hachad cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Jardin d'or",
      "Sector of Activity": "- restauration - pizza et chawarma",
      "Address": "27 complexe commercial tawada front de mer - Agadir (M)"
    },
    {
      "Company Name": "Ste ideal editions 2000",
      "Sector of Activity": "- travaux d'imprimerie",
      "Address": "31 bloc 65 sidi othmane - Casablanca"
    },
    {
      "Company Name": "World park (ste)",
      "Sector of Activity": "Gestion realisations de parks d'attractions",
      "Address": "Av des far 10 eme etage - Casablanca"
    },
    {
      "Company Name": "Diffusion kenzy",
      "Sector of Activity": "Fabricant de vetements confectionnes-md import export",
      "Address": "19 imm - cb rue abou abbès azfi - El Maarif (AR)"
    },
    {
      "Company Name": "Majestic hotels limited (ste)",
      "Sector of Activity": "Societe hoteliere",
      "Address": "Hotel amphitrite - Skhirate- Temara"
    },
    {
      "Company Name": "Global market components (ste)",
      "Sector of Activity": "La commercialisation, l'importation et l'exportation de materiel informatique, electronique, peripheriques et accessoires",
      "Address": "5 rue bouiblane - Rabat"
    },
    {
      "Company Name": "Point sud",
      "Sector of Activity": "Agence de voyage tourisme",
      "Address": "Complexe anzi n?4 bd. mohamed v - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Rimal vacance services (RVS)",
      "Sector of Activity": "Transport touristique",
      "Address": "408, bd mohamed zerktouni, résid. elistikrare, 2°ét. - Casablanca"
    },
    {
      "Company Name": "Menuiserie ebenisterie france ville",
      "Sector of Activity": "La menuiserie et ebenesterie",
      "Address": "N?37 bd. farhat hachad cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Jardin d'or",
      "Sector of Activity": "- restauration - pizza et chawarma",
      "Address": "27 complexe commercial tawada front de mer - Agadir (M)"
    },
    {
      "Company Name": "Ste ideal editions 2000",
      "Sector of Activity": "- travaux d'imprimerie",
      "Address": "31 bloc 65 sidi othmane - Casablanca"
    },
    {
      "Company Name": "World park (ste)",
      "Sector of Activity": "Gestion realisations de parks d'attractions",
      "Address": "Av des far 10 eme etage - Casablanca"
    },
    {
      "Company Name": "Diffusion kenzy",
      "Sector of Activity": "Fabricant de vetements confectionnes-md import export",
      "Address": "19 imm - cb rue abou abbès azfi - El Maarif (AR)"
    },
    {
      "Company Name": "Majestic hotels limited (ste)",
      "Sector of Activity": "Societe hoteliere",
      "Address": "Hotel amphitrite - Skhirate- Temara"
    },
    {
      "Company Name": "Global market components (ste)",
      "Sector of Activity": "La commercialisation, l'importation et l'exportation de materiel informatique, electronique, peripheriques et accessoires",
      "Address": "5 rue bouiblane - Rabat"
    },
    {
      "Company Name": "Dar el hijra et de travaux (DALHIT)",
      "Sector of Activity": "Entrepreneur de travaux divers",
      "Address": "Lotissement el fath n52 appt. 3 - Skhirate- Temara"
    },
    {
      "Company Name": "Rimal vacance services (RVS)",
      "Sector of Activity": "Transport touristique",
      "Address": "408, bd mohamed zerktouni, résid. elistikrare, 2°ét. - Casablanca"
    },
    {
      "Company Name": "Menuiserie ebenisterie france ville",
      "Sector of Activity": "La menuiserie et ebenesterie",
      "Address": "N?37 bd. farhat hachad cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Jardin d'or",
      "Sector of Activity": "- restauration - pizza et chawarma",
      "Address": "27 complexe commercial tawada front de mer - Agadir (M)"
    },
    {
      "Company Name": "Ste ideal editions 2000",
      "Sector of Activity": "- travaux d'imprimerie",
      "Address": "31 bloc 65 sidi othmane - Casablanca"
    },
    {
      "Company Name": "World park (ste)",
      "Sector of Activity": "Gestion realisations de parks d'attractions",
      "Address": "Av des far 10 eme etage - Casablanca"
    },
    {
      "Company Name": "Diffusion kenzy",
      "Sector of Activity": "Fabricant de vetements confectionnes-md import export",
      "Address": "19 imm - cb rue abou abbès azfi - El Maarif (AR)"
    },
    {
      "Company Name": "Majestic hotels limited (ste)",
      "Sector of Activity": "Societe hoteliere",
      "Address": "Hotel amphitrite - Skhirate- Temara"
    },
    {
      "Company Name": "Global market components (ste)",
      "Sector of Activity": "La commercialisation, l'importation et l'exportation de materiel informatique, electronique, peripheriques et accessoires",
      "Address": "5 rue bouiblane - Rabat"
    },
    {
      "Company Name": "Dar el hijra et de travaux (DALHIT)",
      "Sector of Activity": "Entrepreneur de travaux divers",
      "Address": "Lotissement el fath n52 appt. 3 - Skhirate- Temara"
    },
    {
      "Company Name": "Dreft food et drink",
      "Sector of Activity": "Vente de produits alimentaires",
      "Address": "Lot attasni al massira lot n52 zone industrielle - Skhirate- Temara"
    },
    {
      "Company Name": "Menuiserie ebenisterie france ville",
      "Sector of Activity": "La menuiserie et ebenesterie",
      "Address": "N?37 bd. farhat hachad cite dakhla - Agadir-Ida Ou Tanane"
    },
    {
      "Company Name": "Jardin d'or",
      "Sector of Activity": "- restauration - pizza et chawarma",
      "Address": "27 complexe commercial tawada front de mer - Agadir (M)"
    },
    {
      "Company Name": "Ste ideal editions 2000",
      "Sector of Activity": "- travaux d'imprimerie",
      "Address": "31 bloc 65 sidi othmane - Casablanca"
    },
    {
      "Company Name": "World park (ste)",
      "Sector of Activity": "Gestion realisations de parks d'attractions",
      "Address": "Av des far 10 eme etage - Casablanca"
    },
    {
      "Company Name": "Diffusion kenzy",
      "Sector of Activity": "Fabricant de vetements confectionnes-md import export",
      "Address": "19 imm - cb rue abou abbès azfi - El Maarif (AR)"
    },
    {
      "Company Name": "Majestic hotels limited (ste)",
      "Sector of Activity": "Societe hoteliere",
      "Address": "Hotel amphitrite - Skhirate- Temara"
    },
    {
      "Company Name": "Global market components (ste)",
      "Sector of Activity": "La commercialisation, l'importation et l'exportation de materiel informatique, electronique, peripheriques et accessoires",
      "Address": "5 rue bouiblane - Rabat"
    },
    {
      "Company Name": "Dar el hijra et de travaux (DALHIT)",
      "Sector of Activity": "Entrepreneur de travaux divers",
      "Address": "Lotissement el fath n52 appt. 3 - Skhirate- Temara"
    },
    {
      "Company Name": "Dreft food et drink",
      "Sector of Activity": "Vente de produits alimentaires",
      "Address": "Lot attasni al massira lot n52 zone industrielle - Skhirate- Temara"
    },
    {
      "Company Name": "Isosem (ste)",
      "Sector of Activity": "Import export de produit d'isolation de batiment",
      "Address": "16 palce de russie appt 9 ocean - Rabat"
    },
    {
      "Company Name": "Jardin d'or",
      "Sector of Activity": "- restauration - pizza et chawarma",
      "Address": "27 complexe commercial tawada front de mer - Agadir (M)"
    },
    {
      "Company Name": "Ste ideal editions 2000",
      "Sector of Activity": "- travaux d'imprimerie",
      "Address": "31 bloc 65 sidi othmane - Casablanca"
    },
    {
      "Company Name": "World park (ste)",
      "Sector of Activity": "Gestion realisations de parks d'attractions",
      "Address": "Av des far 10 eme etage - Casablanca"
    },
    {
      "Company Name": "Diffusion kenzy",
      "Sector of Activity": "Fabricant de vetements confectionnes-md import export",
      "Address": "19 imm - cb rue abou abbès azfi - El Maarif (AR)"
    },
    {
      "Company Name": "Majestic hotels limited (ste)",
      "Sector of Activity": "Societe hoteliere",
      "Address": "Hotel amphitrite - Skhirate- Temara"
    },
    {
      "Company Name": "Global market components (ste)",
      "Sector of Activity": "La commercialisation, l'importation et l'exportation de materiel informatique, electronique, peripheriques et accessoires",
      "Address": "5 rue bouiblane - Rabat"
    },
    {
      "Company Name": "Dar el hijra et de travaux (DALHIT)",
      "Sector of Activity": "Entrepreneur de travaux divers",
      "Address": "Lotissement el fath n52 appt. 3 - Skhirate- Temara"
    },
    {
      "Company Name": "Dreft food et drink",
      "Sector of Activity": "Vente de produits alimentaires",
      "Address": "Lot attasni al massira lot n52 zone industrielle - Skhirate- Temara"
    },
    {
      "Company Name": "Isosem (ste)",
      "Sector of Activity": "Import export de produit d'isolation de batiment",
      "Address": "16 palce de russie appt 9 ocean - Rabat"
    },
    {
      "Company Name": "Afi mode patisserie",
      "Sector of Activity": "Ecole de formation professionnelle",
      "Address": "25 rue aguelmane sidi ali - Rabat"
    },
    {
      "Company Name": "Ste ideal editions 2000",
      "Sector of Activity": "- travaux d'imprimerie",
      "Address": "31 bloc 65 sidi othmane - Casablanca"
    },
    {
      "Company Name": "World park (ste)",
      "Sector of Activity": "Gestion realisations de parks d'attractions",
      "Address": "Av des far 10 eme etage - Casablanca"
    },
    {
      "Company Name": "Diffusion kenzy",
      "Sector of Activity": "Fabricant de vetements confectionnes-md import export",
      "Address": "19 imm - cb rue abou abbès azfi - El Maarif (AR)"
    },
    {
      "Company Name": "Majestic hotels limited (ste)",
      "Sector of Activity": "Societe hoteliere",
      "Address": "Hotel amphitrite - Skhirate- Temara"
    },
    {
      "Company Name": "Global market components (ste)",
      "Sector of Activity": "La commercialisation, l'importation et l'exportation de materiel informatique, electronique, peripheriques et accessoires",
      "Address": "5 rue bouiblane - Rabat"
    },
    {
      "Company Name": "Dar el hijra et de travaux (DALHIT)",
      "Sector of Activity": "Entrepreneur de travaux divers",
      "Address": "Lotissement el fath n52 appt. 3 - Skhirate- Temara"
    },
    {
      "Company Name": "Dreft food et drink",
      "Sector of Activity": "Vente de produits alimentaires",
      "Address": "Lot attasni al massira lot n52 zone industrielle - Skhirate- Temara"
    },
    {
      "Company Name": "Isosem (ste)",
      "Sector of Activity": "Import export de produit d'isolation de batiment",
      "Address": "16 palce de russie appt 9 ocean - Rabat"
    },
    {
      "Company Name": "Afi mode patisserie",
      "Sector of Activity": "Ecole de formation professionnelle",
      "Address": "25 rue aguelmane sidi ali - Rabat"
    },
    {
      "Company Name": "Bena/i-co (ste)",
      "Sector of Activity": "Construction, equipement et amenagement exterieur",
      "Address": "Groupe 68 n 7 bouitat cym - Rabat"
    },
    {
      "Company Name": "World park (ste)",
      "Sector of Activity": "Gestion realisations de parks d'attractions",
      "Address": "Av des far 10 eme etage - Casablanca"
    },
    {
      "Company Name": "Diffusion kenzy",
      "Sector of Activity": "Fabricant de vetements confectionnes-md import export",
      "Address": "19 imm - cb rue abou abbès azfi - El Maarif (AR)"
    },
    {
      "Company Name": "Majestic hotels limited (ste)",
      "Sector of Activity": "Societe hoteliere",
      "Address": "Hotel amphitrite - Skhirate- Temara"
    },
    {
      "Company Name": "Global market components (ste)",
      "Sector of Activity": "La commercialisation, l'importation et l'exportation de materiel informatique, electronique, peripheriques et accessoires",
      "Address": "5 rue bouiblane - Rabat"
    },
    {
      "Company Name": "Dar el hijra et de travaux (DALHIT)",
      "Sector of Activity": "Entrepreneur de travaux divers",
      "Address": "Lotissement el fath n52 appt. 3 - Skhirate- Temara"
    },
    {
      "Company Name": "Dreft food et drink",
      "Sector of Activity": "Vente de produits alimentaires",
      "Address": "Lot attasni al massira lot n52 zone industrielle - Skhirate- Temara"
    },
    {
      "Company Name": "Isosem (ste)",
      "Sector of Activity": "Import export de produit d'isolation de batiment",
      "Address": "16 palce de russie appt 9 ocean - Rabat"
    },
    {
      "Company Name": "Afi mode patisserie",
      "Sector of Activity": "Ecole de formation professionnelle",
      "Address": "25 rue aguelmane sidi ali - Rabat"
    },
    {
      "Company Name": "Bena/i-co (ste)",
      "Sector of Activity": "Construction, equipement et amenagement exterieur",
      "Address": "Groupe 68 n 7 bouitat cym - Rabat"
    },
    {
      "Company Name": "Cosy house (ste)",
      "Sector of Activity": "Promotion immobiliere",
      "Address": "N6 rue ibn hajjar appt n3 - Rabat"
    },
    {
      "Company Name": "Diffusion kenzy",
      "Sector of Activity": "Fabricant de vetements confectionnes-md import export",
      "Address": "19 imm - cb rue abou abbès azfi - El Maarif (AR)"
    },
    {
      "Company Name": "Majestic hotels limited (ste)",
      "Sector of Activity": "Societe hoteliere",
      "Address": "Hotel amphitrite - Skhirate- Temara"
    },
    {
      "Company Name": "Global market components (ste)",
      "Sector of Activity": "La commercialisation, l'importation et l'exportation de materiel informatique, electronique, peripheriques et accessoires",
      "Address": "5 rue bouiblane - Rabat"
    },
    {
      "Company Name": "Dar el hijra et de travaux (DALHIT)",
      "Sector of Activity": "Entrepreneur de travaux divers",
      "Address": "Lotissement el fath n52 appt. 3 - Skhirate- Temara"
    },
    {
      "Company Name": "Dreft food et drink",
      "Sector of Activity": "Vente de produits alimentaires",
      "Address": "Lot attasni al massira lot n52 zone industrielle - Skhirate- Temara"
    },
    {
      "Company Name": "Isosem (ste)",
      "Sector of Activity": "Import export de produit d'isolation de batiment",
      "Address": "16 palce de russie appt 9 ocean - Rabat"
    },
    {
      "Company Name": "Afi mode patisserie",
      "Sector of Activity": "Ecole de formation professionnelle",
      "Address": "25 rue aguelmane sidi ali - Rabat"
    },
    {
      "Company Name": "Bena/i-co (ste)",
      "Sector of Activity": "Construction, equipement et amenagement exterieur",
      "Address": "Groupe 68 n 7 bouitat cym - Rabat"
    },
    {
      "Company Name": "Cosy house (ste)",
      "Sector of Activity": "Promotion immobiliere",
      "Address": "N6 rue ibn hajjar appt n3 - Rabat"
    },
    {
      "Company Name": "Mer (tresors de)",
      "Sector of Activity": "Vente et achat en demi-gros, en gros et en detail de produits de peche marocain a l'etat frais, congeles, entiers ou decoupes (traiteur)",
      "Address": "14 av michlifen magasin n3 - Rabat"
    },
    {
      "Company Name": "Majestic hotels limited (ste)",
      "Sector of Activity": "Societe hoteliere",
      "Address": "Hotel amphitrite - Skhirate- Temara"
    },
    {
      "Company Name": "Global market components (ste)",
      "Sector of Activity": "La commercialisation, l'importation et l'exportation de materiel informatique, electronique, peripheriques et accessoires",
      "Address": "5 rue bouiblane - Rabat"
    },
    {
      "Company Name": "Dar el hijra et de travaux (DALHIT)",
      "Sector of Activity": "Entrepreneur de travaux divers",
      "Address": "Lotissement el fath n52 appt. 3 - Skhirate- Temara"
    },
    {
      "Company Name": "Dreft food et drink",
      "Sector of Activity": "Vente de produits alimentaires",
      "Address": "Lot attasni al massira lot n52 zone industrielle - Skhirate- Temara"
    },
    {
      "Company Name": "Isosem (ste)",
      "Sector of Activity": "Import export de produit d'isolation de batiment",
      "Address": "16 palce de russie appt 9 ocean - Rabat"
    },
    {
      "Company Name": "Afi mode patisserie",
      "Sector of Activity": "Ecole de formation professionnelle",
      "Address": "25 rue aguelmane sidi ali - Rabat"
    },
    {
      "Company Name": "Bena/i-co (ste)",
      "Sector of Activity": "Construction, equipement et amenagement exterieur",
      "Address": "Groupe 68 n 7 bouitat cym - Rabat"
    },
    {
      "Company Name": "Cosy house (ste)",
      "Sector of Activity": "Promotion immobiliere",
      "Address": "N6 rue ibn hajjar appt n3 - Rabat"
    },
    {
      "Company Name": "Mer (tresors de)",
      "Sector of Activity": "Vente et achat en demi-gros, en gros et en detail de produits de peche marocain a l'etat frais, congeles, entiers ou decoupes (traiteur)",
      "Address": "14 av michlifen magasin n3 - Rabat"
    },
    {
      "Company Name": "Glob accounting (ste)",
      "Sector of Activity": "Travaux de comptabilite et divers",
      "Address": "6 rue my hfid appt 26 place pietrie - Rabat"
    },
    {
      "Company Name": "Global market components (ste)",
      "Sector of Activity": "La commercialisation, l'importation et l'exportation de materiel informatique, electronique, peripheriques et accessoires",
      "Address": "5 rue bouiblane - Rabat"
    },
    {
      "Company Name": "Dar el hijra et de travaux (DALHIT)",
      "Sector of Activity": "Entrepreneur de travaux divers",
      "Address": "Lotissement el fath n52 appt. 3 - Skhirate- Temara"
    },
    {
      "Company Name": "Dreft food et drink",
      "Sector of Activity": "Vente de produits alimentaires",
      "Address": "Lot attasni al massira lot n52 zone industrielle - Skhirate- Temara"
    },
    {
      "Company Name": "Isosem (ste)",
      "Sector of Activity": "Import export de produit d'isolation de batiment",
      "Address": "16 palce de russie appt 9 ocean - Rabat"
    },
    {
      "Company Name": "Afi mode patisserie",
      "Sector of Activity": "Ecole de formation professionnelle",
      "Address": "25 rue aguelmane sidi ali - Rabat"
    },
    {
      "Company Name": "Bena/i-co (ste)",
      "Sector of Activity": "Construction, equipement et amenagement exterieur",
      "Address": "Groupe 68 n 7 bouitat cym - Rabat"
    },
    {
      "Company Name": "Cosy house (ste)",
      "Sector of Activity": "Promotion immobiliere",
      "Address": "N6 rue ibn hajjar appt n3 - Rabat"
    },
    {
      "Company Name": "Mer (tresors de)",
      "Sector of Activity": "Vente et achat en demi-gros, en gros et en detail de produits de peche marocain a l'etat frais, congeles, entiers ou decoupes (traiteur)",
      "Address": "14 av michlifen magasin n3 - Rabat"
    },
    {
      "Company Name": "Glob accounting (ste)",
      "Sector of Activity": "Travaux de comptabilite et divers",
      "Address": "6 rue my hfid appt 26 place pietrie - Rabat"
    },
    {
      "Company Name": "Jour de lumiere (JDL)",
      "Sector of Activity": "- commerce de détail de quincaillerie - droguerie - commerce de gros de matériel électrique et électronique",
      "Address": "09 rue patrice lumumba - hassane - Hassan (AR)"
    },
    {
      "Company Name": "Dar el hijra et de travaux (DALHIT)",
      "Sector of Activity": "Entrepreneur de travaux divers",
      "Address": "Lotissement el fath n52 appt. 3 - Skhirate- Temara"
    },
    {
      "Company Name": "Dreft food et drink",
      "Sector of Activity": "Vente de produits alimentaires",
      "Address": "Lot attasni al massira lot n52 zone industrielle - Skhirate- Temara"
    },
    {
      "Company Name": "Isosem (ste)",
      "Sector of Activity": "Import export de produit d'isolation de batiment",
      "Address": "16 palce de russie appt 9 ocean - Rabat"
    },
    {
      "Company Name": "Afi mode patisserie",
      "Sector of Activity": "Ecole de formation professionnelle",
      "Address": "25 rue aguelmane sidi ali - Rabat"
    },
    {
      "Company Name": "Bena/i-co (ste)",
      "Sector of Activity": "Construction, equipement et amenagement exterieur",
      "Address": "Groupe 68 n 7 bouitat cym - Rabat"
    },
    {
      "Company Name": "Cosy house (ste)",
      "Sector of Activity": "Promotion immobiliere",
      "Address": "N6 rue ibn hajjar appt n3 - Rabat"
    },
    {
      "Company Name": "Mer (tresors de)",
      "Sector of Activity": "Vente et achat en demi-gros, en gros et en detail de produits de peche marocain a l'etat frais, congeles, entiers ou decoupes (traiteur)",
      "Address": "14 av michlifen magasin n3 - Rabat"
    },
    {
      "Company Name": "Glob accounting (ste)",
      "Sector of Activity": "Travaux de comptabilite et divers",
      "Address": "6 rue my hfid appt 26 place pietrie - Rabat"
    },
    {
      "Company Name": "Jour de lumiere (JDL)",
      "Sector of Activity": "- commerce de détail de quincaillerie - droguerie - commerce de gros de matériel électrique et électronique",
      "Address": "09 rue patrice lumumba - hassane - Hassan (AR)"
    },
    {
      "Company Name": "Ikrame allah (ste)",
      "Sector of Activity": "Transport de voyageur et des travaux divers import de toutes produits commerciaux et informatique",
      "Address": "Av imam malik km 8 route des zaers n14 - Rabat"
    },
    {
      "Company Name": "Dreft food et drink",
      "Sector of Activity": "Vente de produits alimentaires",
      "Address": "Lot attasni al massira lot n52 zone industrielle - Skhirate- Temara"
    },
    {
      "Company Name": "Isosem (ste)",
      "Sector of Activity": "Import export de produit d'isolation de batiment",
      "Address": "16 palce de russie appt 9 ocean - Rabat"
    },
    {
      "Company Name": "Afi mode patisserie",
      "Sector of Activity": "Ecole de formation professionnelle",
      "Address": "25 rue aguelmane sidi ali - Rabat"
    },
    {
      "Company Name": "Bena/i-co (ste)",
      "Sector of Activity": "Construction, equipement et amenagement exterieur",
      "Address": "Groupe 68 n 7 bouitat cym - Rabat"
    },
    {
      "Company Name": "Cosy house (ste)",
      "Sector of Activity": "Promotion immobiliere",
      "Address": "N6 rue ibn hajjar appt n3 - Rabat"
    },
    {
      "Company Name": "Mer (tresors de)",
      "Sector of Activity": "Vente et achat en demi-gros, en gros et en detail de produits de peche marocain a l'etat frais, congeles, entiers ou decoupes (traiteur)",
      "Address": "14 av michlifen magasin n3 - Rabat"
    },
    {
      "Company Name": "Glob accounting (ste)",
      "Sector of Activity": "Travaux de comptabilite et divers",
      "Address": "6 rue my hfid appt 26 place pietrie - Rabat"
    },
    {
      "Company Name": "Jour de lumiere (JDL)",
      "Sector of Activity": "- commerce de détail de quincaillerie - droguerie - commerce de gros de matériel électrique et électronique",
      "Address": "09 rue patrice lumumba - hassane - Hassan (AR)"
    },
    {
      "Company Name": "Ikrame allah (ste)",
      "Sector of Activity": "Transport de voyageur et des travaux divers import de toutes produits commerciaux et informatique",
      "Address": "Av imam malik km 8 route des zaers n14 - Rabat"
    },
    {
      "Company Name": "Cve informatique (ste) (CVEI)",
      "Sector of Activity": "Vente maintenance materiel informatique bureautique",
      "Address": "9 rue moha et hammou zayani appt 3 ksibat - Rabat"
    },
    {
      "Company Name": "Isosem (ste)",
      "Sector of Activity": "Import export de produit d'isolation de batiment",
      "Address": "16 palce de russie appt 9 ocean - Rabat"
    },
    {
      "Company Name": "Afi mode patisserie",
      "Sector of Activity": "Ecole de formation professionnelle",
      "Address": "25 rue aguelmane sidi ali - Rabat"
    },
    {
      "Company Name": "Bena/i-co (ste)",
      "Sector of Activity": "Construction, equipement et amenagement exterieur",
      "Address": "Groupe 68 n 7 bouitat cym - Rabat"
    },
    {
      "Company Name": "Cosy house (ste)",
      "Sector of Activity": "Promotion immobiliere",
      "Address": "N6 rue ibn hajjar appt n3 - Rabat"
    },
    {
      "Company Name": "Mer (tresors de)",
      "Sector of Activity": "Vente et achat en demi-gros, en gros et en detail de produits de peche marocain a l'etat frais, congeles, entiers ou decoupes (traiteur)",
      "Address": "14 av michlifen magasin n3 - Rabat"
    },
    {
      "Company Name": "Glob accounting (ste)",
      "Sector of Activity": "Travaux de comptabilite et divers",
      "Address": "6 rue my hfid appt 26 place pietrie - Rabat"
    },
    {
      "Company Name": "Jour de lumiere (JDL)",
      "Sector of Activity": "- commerce de détail de quincaillerie - droguerie - commerce de gros de matériel électrique et électronique",
      "Address": "09 rue patrice lumumba - hassane - Hassan (AR)"
    },
    {
      "Company Name": "Ikrame allah (ste)",
      "Sector of Activity": "Transport de voyageur et des travaux divers import de toutes produits commerciaux et informatique",
      "Address": "Av imam malik km 8 route des zaers n14 - Rabat"
    },
    {
      "Company Name": "Cve informatique (ste) (CVEI)",
      "Sector of Activity": "Vente maintenance materiel informatique bureautique",
      "Address": "9 rue moha et hammou zayani appt 3 ksibat - Rabat"
    },
    {
      "Company Name": "Igmir aluminium (ste)",
      "Sector of Activity": "Travaux d'aluminium",
      "Address": "101 cigal cigalon - Skhirate- Temara"
    },
    {
      "Company Name": "Afi mode patisserie",
      "Sector of Activity": "Ecole de formation professionnelle",
      "Address": "25 rue aguelmane sidi ali - Rabat"
    },
    {
      "Company Name": "Bena/i-co (ste)",
      "Sector of Activity": "Construction, equipement et amenagement exterieur",
      "Address": "Groupe 68 n 7 bouitat cym - Rabat"
    },
    {
      "Company Name": "Cosy house (ste)",
      "Sector of Activity": "Promotion immobiliere",
      "Address": "N6 rue ibn hajjar appt n3 - Rabat"
    },
    {
      "Company Name": "Mer (tresors de)",
      "Sector of Activity": "Vente et achat en demi-gros, en gros et en detail de produits de peche marocain a l'etat frais, congeles, entiers ou decoupes (traiteur)",
      "Address": "14 av michlifen magasin n3 - Rabat"
    },
  ]

# Project metadata
project = {
    "Theme": "caravane",
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

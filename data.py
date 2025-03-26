import requests
from bs4 import BeautifulSoup
import csv
import os

# URL du joueur de volley
player_url = "https://en.volleyballworld.com/volleyball/competitions/volleyball-olympic-games-paris-2024/players/142686"

# Récupérer la page HTML du joueur
response = requests.get(player_url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    print("Requête réussie")
    player_soup = BeautifulSoup(response.text, "html.parser")
    
    # Trouver toutes les divs avec la classe vbw-player-bio-text
    bio_text_divs = player_soup.find_all("div", class_="vbw-player-bio-text")

    # Extraire les valeurs des divs
    if len(bio_text_divs) > 0:
        position = bio_text_divs[0].text.strip()
    else:
        position = "Non renseigné"

    if len(bio_text_divs) > 1:
        pos = bio_text_divs[1].text.strip()
    else:
        pos = "Non renseigné"

    if len(bio_text_divs) > 2:
        nationality = bio_text_divs[2].text.strip()
    else:
        nationality = "Non renseigné"

    if len(bio_text_divs) > 3:
        nat = bio_text_divs[3].text.strip()
    else:
        nat = "Non renseigné"

    if len(bio_text_divs) > 4:
        age = bio_text_divs[4].text.strip()
    else:
        age = "Non renseigné"

    if len(bio_text_divs) > 5:
        birth_date = bio_text_divs[5].text.strip()
    else:
        birth_date = "Non renseigné"

    if len(bio_text_divs) > 6:
        height = bio_text_divs[6].text.strip()
    else:
        height = "Non renseigné"

    # Vérifier si le fichier CSV existe déjà
    file_exists = os.path.isfile('dataPlayer.csv')

    # Ouvrir le fichier CSV pour écrire les valeurs trouvées
    with open('dataPlayer.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Écrire l'en-tête si le fichier n'existe pas
        if not file_exists:
            writer.writerow(["Position", "Pos", "Nationality", "Nat", "Age", "Birth Date", "Height"])
        
        # Écrire les valeurs trouvées dans le fichier CSV
        writer.writerow([position, pos, nationality, nat, age, birth_date, height])
else:
    print(f"Échec de la requête. Statut HTTP : {response.status_code}")
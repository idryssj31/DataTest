import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL de la page à scraper
url = 'https://en.volleyballworld.com/volleyball/competitions/volleyball-nations-league/2022/finals-statistics/men/best-receivers/'

# Envoyer une requête GET à la page
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    print("Page retrieved successfully")
    
    # Parser le contenu HTML de la page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Afficher le contenu HTML pour vérifier la structure
    # print(soup.prettify())  # Décommentez cette ligne pour afficher le contenu HTML
    
    # Trouver les éléments contenant les informations des joueurs
    players = soup.select('.box_content')
    
    # Vérifier si des joueurs ont été trouvés
    if players:
        print(f"Found {len(players)} players")
        
        # Extraire et afficher le contenu de chaque balise div avec la classe box_content
        for player in players:
            print(player.get_text(strip=True))
    else:
        print("No players found with the given selector")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Chemin du répertoire contenant les fichiers CSV
directory = r'c:\Users\idrys\DataTest'

# Parcourir tous les fichiers dans le répertoire
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(root, file)
            try:
                # Lire le fichier CSV
                df = pd.read_csv(file_path)
                
                # Vérifier si les colonnes existent dans le fichier CSV
                if 'web-scraper-order' in df.columns and 'web-scraper-start-url' in df.columns:
                    # Supprimer les colonnes 'web-scraper-order' et 'web-scraper-start-url'
                    df = df.drop(columns=['web-scraper-order', 'web-scraper-start-url'])
                    
                    # Sauvegarder le fichier CSV modifié
                    df.to_csv(file_path, index=False)
                    print(f"Updated file: {file_path}")
                else:
                    print(f"Columns not found in file: {file_path}")
            except Exception as e:
                print(f"Failed to process file: {file_path}. Error: {e}")
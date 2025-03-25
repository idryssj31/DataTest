import requests
from bs4 import BeautifulSoup
import pandas as pd

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

# Lire le fichier CSV
df = pd.read_csv(r'c:\Users\idrys\DataTest\JO\JOTROPHIES\jotrophies2024.csv')

# Supprimer les colonnes 'web-scraper-order' et 'web-scraper-start-url'
df = df.drop(columns=['web-scraper-order', 'web-scraper-start-url'])

# Sauvegarder le fichier CSV modifié
df.to_csv(r'c:\Users\idrys\DataTest\JO\JOTROPHIES\jotrophies2024_modified.csv', index=False)
import requests
from bs4 import BeautifulSoup
import subprocess

# URL de la liste des joueurs
url = "https://en.volleyballworld.com/volleyball/competitions/volleyball-olympic-games-paris-2024/teams/men/6622/players/"

# Récupérer la page HTML
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    print("Requête réussie")
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Trouver le tbody avec la classe vbw-o-table__body
    tbody = soup.find("tbody", class_="vbw-o-table__body")
    
    # Trouver toutes les balises tr dans le tbody
    rows = tbody.find_all("tr")
    
    # Pour chaque balise tr, récupérer l'URL du joueur
    for row in rows:
        player_td = row.find("td", class_="vbw-o-table__cell playername")
        if player_td:
            player_link = player_td.find("a", class_="d3-l-col__col-2")
            if player_link and 'href' in player_link.attrs:
                player_url = f"https://en.volleyballworld.com{player_link['href']}"
                print(player_url)
                
                # Lire le contenu de data.py
                with open('g:\\Dev Web\\Ynov\\M1\\Ydays\\Valab\\DataTest\\data.py', 'r') as file:
                    data = file.readlines()
                
                # Remplacer la valeur de player_url
                for i, line in enumerate(data):
                    if line.startswith("player_url ="):
                        data[i] = f'player_url = "{player_url}"\n'
                
                # Écrire le contenu mis à jour dans data.py
                with open('g:\\Dev Web\\Ynov\\M1\\Ydays\\Valab\\DataTest\\data.py', 'w') as file:
                    file.writelines(data)
                
                # Exécuter data.py
                subprocess.run(["python", "g:\\Dev Web\\Ynov\\M1\\Ydays\\Valab\\DataTest\\data.py"])
else:
    print(f"Échec de la requête. Statut HTTP : {response.status_code}")
import requests
from bs4 import BeautifulSoup
import subprocess

# URL de la liste des équipes
team_list_url = "https://en.volleyballworld.com/volleyball/competitions/volleyball-olympic-games-paris-2024/teams/men/"

# Récupérer la page HTML de la liste des équipes
response = requests.get(team_list_url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    print("Requête réussie")
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Trouver la div avec la classe d3-l-grid--inner
    grid_inner_div = soup.find("div", class_="d3-l-grid--inner")
    
    # Trouver toutes les balises a avec la classe d3-l-col__col-2
    team_links = grid_inner_div.find_all("a", class_="d3-l-col__col-2")
    
    # Pour chaque balise a, récupérer l'URL de l'équipe
    for team_link in team_links:
        team_url = f"https://en.volleyballworld.com{team_link['href']}"
        print(f"URL de l'équipe : {team_url}")
        
        # Récupérer la page HTML de l'équipe
        team_response = requests.get(team_url)
        
        # Vérifier si la requête a réussi
        if team_response.status_code == 200:
            team_soup = BeautifulSoup(team_response.text, "html.parser")
            
            # Trouver la ul avec la classe d3-o-nav__list d3-o-list d3-o-nav__list--buttons
            nav_list_ul = team_soup.find("ul", class_="d3-o-nav__list d3-o-list d3-o-nav__list--buttons")
            
            # Vérifier si la ul existe
            if nav_list_ul:
                # Trouver la première li avec la classe d3-o-nav__item
                first_nav_item = nav_list_ul.find("li", class_="d3-o-nav__item")
                
                # Vérifier si la li existe
                if first_nav_item:
                    # Trouver la balise a dans la li et récupérer l'URL
                    nav_item_link = first_nav_item.find("a")
                    if nav_item_link and 'href' in nav_item_link.attrs:
                        nav_item_url = f"https://en.volleyballworld.com{nav_item_link['href']}"
                        print(f"URL de la première li : {nav_item_url}")
                        
                        # Lire le contenu de page.py
                        with open('g:\\Dev Web\\Ynov\\M1\\Ydays\\Valab\\DataTest\\page.py', 'r') as file:
                            data = file.readlines()
                        
                        # Remplacer la valeur de url
                        for i, line in enumerate(data):
                            if line.startswith("url ="):
                                data[i] = f'url = "{nav_item_url}"\n'
                        
                        # Écrire le contenu mis à jour dans page.py
                        with open('g:\\Dev Web\\Ynov\\M1\\Ydays\\Valab\\DataTest\\page.py', 'w') as file:
                            file.writelines(data)
                        
                        # Exécuter page.py
                        print("Exécution de page.py")
                        result = subprocess.run(["python", "g:\\Dev Web\\Ynov\\M1\\Ydays\\Valab\\DataTest\\page.py"], capture_output=True, text=True)
                        print("Sortie standard :")
                        print(result.stdout)
                        print("Sortie d'erreur :")
                        print(result.stderr)
else:
    print(f"Échec de la requête. Statut HTTP : {response.status_code}")
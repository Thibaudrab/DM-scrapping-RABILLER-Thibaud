import requests
import csv
from bs4 import BeautifulSoup

def recuperer_donnees(page, ecrivain_csv):
    url = f'http://www.scrapethissite.com/pages/forms/?page_num={page}'

    print(f"Récupération des données depuis : {url}")

    reponse = requests.get(url)

    soupe = BeautifulSoup(reponse.content, 'html.parser')

    tableau = soupe.find('table')

    for ligne in tableau.find_all('tr', class_="team"):
        cellules = ligne.find_all('td')
        if cellules:
            nom, annee, victoires, defaites, defaites_ot, pourcentage_victoires, buts_pour, buts_contre, difference_buts = [cell.text.strip() for cell in cellules]

            if int(difference_buts) > 0 and int(buts_contre) < 300:
                ecrivain_csv.writerow([nom, annee, victoires, defaites, defaites_ot, pourcentage_victoires, buts_pour, buts_contre, difference_buts])

with open('resultats.csv', 'w', encoding='UTF8') as fichier_sortie:
    ecrivain_csv = csv.writer(fichier_sortie)
    ecrivain_csv.writerow(['Nom équipe, Année, Victoires, Défaites, Défaites OT, Pourcentage Victoires, Buts pour (BP), Buts contre (BC), +/-'])

    numero_page = 1

    while numero_page <= 10:
        recuperer_donnees(numero_page, ecrivain_csv)
        numero_page += 1

iimport requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

countries = soup.find_all('div', {'class': 'country'})

for country in countries:
    name = country.find('h3').text.strip() if country.find('h3') is not None else ''
    population = country.find('span', {'class': 'country-population'}).text.strip() if country.find('span', {'class': 'country-population'}) is not None else ''
    capital = country.find('span', {'class': 'country-capital'}).text.strip() if country.find('span', {'class': 'country-capital'}) is not None else ''
    area = country.find('span', {'class': 'country-area'}).text.strip() if country.find('span', {'class': 'country-area'}) is not None else ''

    population = population.replace(',', '') if ',' in population else population
    area = area.replace(' km²', '') if ' km²' in area else area

    print('Nom :', name)
    print('Population :', population)
    print('Capitale :', capital)
    print('Aire :', area + " km²")
    print('\n')
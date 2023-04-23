import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

class_selector = "col-md-4 country"
divs = soup.find_all("div", class_=class_selector)

for i, div in enumerate(divs, 1):
    country_name = div.find("h3", class_="country-name").get_text(strip=True)
    capital = div.find("span", class_="country-capital").get_text(strip=True)
    population = div.find("span", class_="country-population").get_text(strip=True)
    area = div.find("span", class_="country-area").get_text(strip=True)

    print(f"Div {i}:")
    print(f"Country Name: {country_name}")
    print(f"Capital: {capital}")
    print(f"Population: {population}")
    print(f"Area: {area}")
    print("-" * 40)

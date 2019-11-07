import json
import requests
from requests import get
from bs4 import BeautifulSoup


url = 'https://pratik.ci/thematiques/loisirs/confiserie'
response = get(url)

response.status_code
# print(response.status_code)
sp = BeautifulSoup(response.text, 'html.parser')
# print(sp)

col12 = sp.find('div', attrs={'class': 'views-row'})
# print(col12)

titre = col12.find('div', attrs={'class': 'field-item even'}).get_text()
print(titre)

telphon1 = col12.find('div', attrs={'class': 'field-name-field-telepone-1'}).get_text()
print(telphon1)

telphon2 = col12.find('div', attrs={'class': 'field-name-field-cellulaire1'}).get_text()
print(telphon2)

addres = col12.find('div', attrs={'class': 'field-name-field-localisation-lieu'}).get_text()
print(addres)

data = {
    'titre': titre,
    'telephone1': telphon1,
    'telephone1': telphon2,
    'adresse': addres,
}

print(data)

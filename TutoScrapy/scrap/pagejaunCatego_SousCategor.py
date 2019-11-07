import requests
from bs4 import BeautifulSoup
from requests import get
import scrap_pagejaune

url = 'https://www.lespagesjaunesafrique.com/{0}'.format(url1)
response = get(url)
print(response.status_code)

# if response.status_code == 200:

#     htmlsoup = BeautifulSoup(response.text, 'html.parser')
#     # --- Récuperation PRESENTATION --- #
    
#     div_prese = htmlsoup.find_all('div', attrs={'class': 'col-sm-4 col-xs-6 col-md-4 col-lg-3'})
    
    
# else:
#     print("Erreur", response.status_code)
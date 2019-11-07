import requests
from bs4 import BeautifulSoup
from requests import get

url = 'http://www.abidjanguide.com/'
response = get(url)
# print(response.status_code)


if response.status_code == 200:
    
    # --- Récuperation HTML --- #
    
    htmlsoup = BeautifulSoup(response.text, 'html.parser')
    
    # --- Récuperation TITRE --- #
    
    div_title = htmlsoup.find('div', attrs={'class': 'navbar-header'})
    h1title = div_title.find('h1')
    #print(h1title.text)
    # print(htmlsoup)
    
    # --- Récuperation PRESENTATION --- #
    
    div_presentation = htmlsoup.find_all('div', attrs={'class': 'col-md-2'})
    div_row = htmlsoup.find_all('div', attrs={'class': 'row'})
    print(div_row)
    
    compt = 1
    # --- Boucle au niveau de div_presentation  --- #
    
    # for item in div_presentation:
    #     if compt < 4:
    #         # --- Récuperation  --- #
    #         ba = item.find('a')
    #         img = ba.find('img')
    #         h3 = ba.find('h3')
            
    #         # --- Affectation  --- #
    #         image = img['src']
    #         url = ba['href']
    #         titre = h3.text
            
            
            # --- Affichage  --- #
            
            #print(item.text)
            # print(compt,  "\n" + "titre: " + titre + "\n"+ "url: " + url + "\n"+ "image: " + image)
            # print(titre)
            # print(url)
            # print(image)
        compt += 1
    # print(div_presentation)
    
    $
    # print(div_presentation)
    
    
else:
    print("Erreur", response.status_code)
    

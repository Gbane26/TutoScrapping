import requests
from bs4 import BeautifulSoup
from requests import get

url = 'https://www.lespagesjaunesafrique.com/'
response = get(url)
print(response.status_code)

if response.status_code == 200:

    htmlsoup = BeautifulSoup(response.text, 'html.parser')
    # --- Récuperation PRESENTATION --- #
    
    div_prese = htmlsoup.find_all('div', attrs={'class': 'col-sm-4 col-xs-6 col-md-4 col-lg-3'})
    
    # div_prese = htmlsoup.find_all('div', attrs={'class': 'drapeaux'})
    # print(div_prese)
    
    compt = 1
    
    for item in div_prese:
        
        ba = item.find('a')
        # print(item.text)
        url1 = ba['href']
        # print(url)
        # print(item.text)
        pays = item.text
        print(compt,  "\n" + "Pays: " + pays + "\n"+ "Lien: " + url1 + "\n")

        compt += 1
    
else:
    print("Erreur", response.status_code)


########### Categorie et SousCategorie #############

print("###################CategorieEtSouSCategorie")

urlcate = 'https://www.lespagesjaunesafrique.com/{0}'.format(url1)
response = get(urlcate)
print(response.status_code)

if response.status_code == 200:
    
    htmlsoup = BeautifulSoup(response.text, 'html.parser')
    # --- Récuperation PRESENTATION --- #
    
    div_categ = htmlsoup.find_all('div', attrs={'class': 'col-sm-12 col-lg-12 ct-u-marginBottom40'})
    # div_textcat = div_categ.find_all('div', attrs={'class': 'activites'})
    # div_prese = htmlsoup.find_all('div', attrs={'class': 'drapeaux'})
    # print(div_categ)
    
    compt = 1
    
    for item in div_categ:
        
        ba = item.find('a')
        urlcat = ba['href']
        cate= item.text
        # print(urlcat)
        print(compt,  "\n" + "Categorie: " + cate + "\n" + "LienCate: " + urlcat + "\n")
        compt += 1
        
else:
    print("Erreur", response.status_code)

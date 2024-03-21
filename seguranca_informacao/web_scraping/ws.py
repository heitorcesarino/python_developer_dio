from bs4 import BeautifulSoup
import requests

#requisição http na url
site = requests.get("https://www.climatempo.com.br/").content

#baixando o html da requisição
soup = BeautifulSoup(site, 'html.parser')

#exibindo html do site
print(soup.prettify())

#pesquisando dentro do html por ocorrencias de determinada classe
temperatura = soup.find("span", class_="icon -circle -recommended common-sprite sprite-recommended")

#exibindo resultado da pesquisa
print(temperatura.string)

#printando a pesquisa pela primeira ocorrencia da tag p
print(soup.p)
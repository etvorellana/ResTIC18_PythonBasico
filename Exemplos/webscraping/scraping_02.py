from selenium import webdriver
from bs4 import BeautifulSoup 
from time import sleep

url = 'https://www.google.com/search?q=cepedi+ilh%C3%A9us'

# Abre o navegador
navegador = webdriver.Chrome()
#navegador = webdriver.Chrome(executable_path='path_to_chromedriver')


navegador.get(url)
#sleep(10)

search = BeautifulSoup(navegador.page_source, 'html.parser')
#print(search.prettify())

search = search.find('div', attrs={'class':'g'})
if search:
    print(search.prettify())
else: 
    print('Nada encontrado')
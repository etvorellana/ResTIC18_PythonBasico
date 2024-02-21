from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep

url = 'https://www.google.com'

# Abre o navegador
navegador = webdriver.Chrome()
#navegador = webdriver.Chrome(executable_path='path_to_chromedriver')

navegador.get(url)
sleep(1)

# Procura o campo de busca
search = navegador.find_element(By.TAG_NAME, "textarea")
if search:
    search.send_keys('cepedi ilhéus')
    sleep(2)
    search.send_keys(Keys.RETURN)
    sleep(1)
else:
    print('Campo de busca não encontrado')

search = BeautifulSoup(navegador.page_source, 'html.parser')
#print(search.prettify())

search = search.find('div', attrs={'class':'g'})
if search:
    print(search.prettify())
else: 
    print('Nada encontrado')

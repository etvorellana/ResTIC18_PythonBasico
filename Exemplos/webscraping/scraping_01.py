import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=cepedi+ilh%C3%A9us'
response = requests.get(url)
search = BeautifulSoup(response.text, 'html.parser')
print(search.prettify())

search = search.find('div', attrs={'class':'g'})
if search:
    print(search.prettify())
else: 
    print('Nada encontrado')

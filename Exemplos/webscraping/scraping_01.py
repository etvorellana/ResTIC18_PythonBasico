import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=cepedi+ilh%C3%A9us'
response = requests.get(url)
search = BeautifulSoup(response.text, 'html.parser')
print(search.prettify())



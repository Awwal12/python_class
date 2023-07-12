# scrap a movie website and get the 'trendings' list
import requests
from bs4 import BeautifulSoup as BS
URL = "https://goku.sx/home"

response = requests.get(URL)
contents = BS(response.text, 'html.parser')
container = contents.find('div', class_='tab-pane show active')
items = container.find_all('div', class_='item')
for item in items:
    name = item.find('h3', class_='movie-name')
    print(name.text)

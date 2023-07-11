from bs4 import BeautifulSoup
import requests

URL = "https://www.jumia.com.ng/sporting-goods/"

response = requests.get(URL)
contents = BeautifulSoup(response.text, 'html.parser')
container = contents.find(
    'div', class_='row _no-g -tac -pvxs -phs _6c-shs')
items = container.find_all('div', class_='ar _3-4')

for item in items:
    name = item.find('div', class_='name')
    print(name.text)
    print()
    price = item.find('div', class_='prc')
    print(price.text)
    print()
    image = item.find('img', class_='img')
    print(image['data-src'])

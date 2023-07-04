import requests

response = requests.get('https://api.publicapis.org/entries')
content = response.json()
print(content['entries'][0]["Description"])

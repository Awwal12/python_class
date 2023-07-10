import requests
url = 'https://api.publicapis.org/entries'
response = requests.get(url)
content = response.json()
print(content['entries'][0]["Description"])

resp = requests.put(
    url, {'userId': 20, 'title': 'Do assessment', 'data': None})
print(resp.json())

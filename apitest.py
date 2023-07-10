import requests
# url = 'https://api.publicapis.org/entries'
# response = requests.get(url)
# content = response.json()
# print(content['entries'][0]["Description"])

# resp = requests.put(
#     url, {'userId': 20, 'title': 'Do assessment', 'data': None})
# print(resp.json())

url = 'https://api-customer-038j.onrender.com/customer/'
response = requests.put(
    url, {'name': 'Whos Jake', 'age': 66, 'order': 'jollof rice'})
resp = requests.get(url)

# print(response.json())
print(resp.json())

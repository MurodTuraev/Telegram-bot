import requests
from pprint import pprint
token = '1597735413:AAEA20RoZ_JJsQ3b4q8XvKuegECeH-i6exk'
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
data = r.json()
updates = data['result']

for update in updates:
    message = update['message']
    first = message['from'].get('first_name', '')
    last = message['from'].get('last_name', '')
    print(first+" "+last)
pprint(data)
print(r.url)

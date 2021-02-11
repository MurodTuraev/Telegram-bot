import requests
from pprint import pprint
token = '11597735413:AAGQsKaIxz8OG4dCyMmzg3KUNOzA1_YE1cQ'
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
data = r.json()
updates = data['result']

for update in updates:
    message = update['message']
    text = message['text']
    first = message['from'].get('first_name')
    print(f'{first} :  {text}')

import requests
import json

token = '1447504211:AAGxb_lBmTjrzWVETUobnQ_zhna-wHR6mrg'
url = f'https://api.telegram.org/bot{token}/getUpdates'
data = requests.get(url).json()
print(data)

import requests
from pprint import pprint
token = '1447504211:AAGxb_lBmTjrzWVETUobnQ_zhna-wHR6mrg'
url = f'https://api.telegram.org/bot{token}/sendMessage'
parametr = {
    'chat_id': 913536871,
    'text': 'salom'
}
r = requests.get(url, params=parametr)
# data = r.json()
pprint(r.url)

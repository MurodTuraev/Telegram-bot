import requests
from pprint import pprint


def getUpdates():
    token = '1447504211:AAGxb_lBmTjrzWVETUobnQ_zhna-wHR6mrg'
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    data = requests.get(url).json()['result']
    return data


def sendMessage(txt, user_id):
    token = '1447504211:AAGxb_lBmTjrzWVETUobnQ_zhna-wHR6mrg'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    parametr = {
        'text': txt,
        'chat_id': user_id
    }
    message = requests.get(url, params=parametr)
    return message


def getmessage(data):
    txt = data[len(data)-1]['message']['text']
    user_id = data[len(data)-1]['message']['from']['id']
    update_id = data[len(data)-1]['update_id']
    return txt, user_id, update_id


n = -1
while True:
    x = getUpdates()
    text, id, update_id = getmessage(x)
    if n != update_id:
        print(text)
        sendMessage(text, id)
        n = update_id

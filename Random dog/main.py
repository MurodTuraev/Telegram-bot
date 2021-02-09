import requests
import json


def getUpdates():
    token = '1595967834:AAGzmibIK5Gz7znUyfmPhR2ZkoYYfrs6Tsg'
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    data = requests.get(url).json()['result'][-1]
    return data


def getuser(data):
    user_id = data['message']['from']['id']
    text = data['message']['text']
    return user_id, text


def photodog():  # random qilib rasm olish
    url = 'https://random.dog/woof.json'
    rasm_url = requests.get(url).json()['url']
    return rasm_url


def sendPhoto(url1, chat_id):
    token = '1595967834:AAGzmibIK5Gz7znUyfmPhR2ZkoYYfrs6Tsg'
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    parametr = {
        'chat_id': chat_id,
        'photo': url1
    }
    photo = requests.get(url, params=parametr)
    return photo


def sendMessage(chat_id):
    token = '1595967834:AAGzmibIK5Gz7znUyfmPhR2ZkoYYfrs6Tsg'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    parametr = {
        'chat_id': chat_id,
        'text': 'Button',
        'reply_markup': {
            'keyboard': [[{'text': '🐶random dog'}]],
            'resize_keyboard': True
        }
    }
    r = requests.post(url, json=parametr)
    return r


message_id = getUpdates()['message']['message_id']
update_id = -1
while True:
    update = getUpdates()
    chat_id, text = getuser(update)
    last_update_id = update['update_id']
    url1 = photodog()
    if text == '🐶random dog':
        if update_id != last_update_id:
            sendPhoto(url1, chat_id)
            update_id = last_update_id
            print(text)
    if update_id != last_update_id:
        if text == '/start':
            sendMessage(chat_id)
            update_id = last_update_id

import requests
import json


def sendPhoto():
    token = '1595967834:AAGzmibIK5Gz7znUyfmPhR2ZkoYYfrs6Tsg'
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    rasm = open('https://random.dog/', 'rb')
    parametr = {
        'chat_id': 913536871,
        # 'photo': 'https://random.dog/ff0b26d5-0ea3-4971-b2cf-9f904f301eef.jpg'
    }
    photo = requests.post(url, params=parametr, files={'photo': rasm})
    return photo


token = '1595967834:AAGzmibIK5Gz7znUyfmPhR2ZkoYYfrs6Tsg'
url = f'https://api.telegram.org/bot{token}/sendMessage'
parametr = {
    'chat_id': 913536871,
    # 'text': 'Button',
    'reply_markup': {
        'keyboard': [[{'text': '🐶random dog'}]],
        'resize_keyboard': True
    }
}
r = requests.post(url, json=parametr)

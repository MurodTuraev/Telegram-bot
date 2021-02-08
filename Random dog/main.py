import requests
import json


def photodog():  # random qilib rasm olish
    url = 'https://random.dog/woof.json'
    rasm_url = requests.get(url).json()['url']
    return rasm_url


def sendPhoto(url1):
    token = '1595967834:AAGzmibIK5Gz7znUyfmPhR2ZkoYYfrs6Tsg'
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    parametr = {
        'chat_id': 913536871,
        'photo': url1
    }
    photo = requests.get(url, params=parametr)
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
sendPhoto(photodog())

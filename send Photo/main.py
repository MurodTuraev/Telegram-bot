import requests
import json
import os
# 913536871
token = os.environ['TOKEN']
url = f'https://api.telegram.org/bot{token}/sendPhoto'

paramet = {
    'chat_id': 913536871,
    'photo': 'https://storage.ws.pho.to/s2/f607aa4c6a291a39cc8c654481fe72568435da6c_m.jpg'
}
r = requests.get(url, params=paramet)

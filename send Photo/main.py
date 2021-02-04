import requests
import json
import os
# 913536871
token = os.environ['TOKEN']
url = f'https://api.telegram.org/bot{token}/sendPhoto'

paramet = {
    'chat_id': 913536871,
    'photo': 'AgACAgIAAxkBAAN4YBunv2JzPeug83nWvfUxLPW_u0MAAo-yMRv-euBIRPfXkgvgjnTMF6KWLgADAQADAgADeQADswQHAAEeBA'
}
r = requests.get(url, params=paramet)

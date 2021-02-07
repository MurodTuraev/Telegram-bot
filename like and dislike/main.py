import requests
import json
from pprint import pprint


def getUpdates():
    token = '1447504211:AAGxb_lBmTjrzWVETUobnQ_zhna-wHR6mrg'
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    data = requests.get(url).json()['result']
    return data


update_id = -1
like = '👍'
dislike = '👎'
count_like=0
count_dislike=0

while True:
    update = getUpdates()
    text = update[-1]['message']['text']
    last_id = update[-1]['update_id']
    user_id=913536871
    for i in update:
        id=i['message']['from']['id']
        if id==user_id:
            if text==like:
                count_like+=1
            elif text==dislike:
                count_dislike+=1
    

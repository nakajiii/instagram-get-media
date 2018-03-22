import json
import requests
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

apiToken = "YOUR API KEY"

def pullapi(hashtagName):
    api = 'https://api.instagram.com/v1/tags/{hashtag}/media/recent?access_token={key}'
    url = api.format(hashtag=hashtagName, key=apiToken)
    
    r = requests.get(url)
    data = json.loads(r.text)

    df = pd.DataFrame(index=[], columns=['post', 'text', 'type', 'likes', 'comments', 'filter', 
                                            'link', 'image', 'user', 'username', 'profile', 'createdtime'])
    
    for i in data['data']:
        se = pd.Series({ 'post' : i['id'],
                   'text' : i['caption']['text'],
                   'type' : i['type'],
                   'likes' : i['likes']['count'],
                   'comments' : i['comments']['count'],
                   'filter' : i['filter'],
                   'link' : i['link'],
                   'image' : i['images']['thumbnail']['url'],
                   'user' : i['user']['id'],
                   'username' : i['user']['username'],
                   'profile' : i['user']['profile_picture'],
                   'createdtime' : i['created_time']})
        df = df.append(se, ignore_index=True)
    return df
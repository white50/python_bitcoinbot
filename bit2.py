import requests,time
import pandas as pd
from datetime import datetime
import os 


def get_OHLC(before,after):
    url = 'https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc'
    query = {
        'periods':60,
        'before':before,
        'after':after,
        }
    res = requests.get(,params=query).json()['result']['60']
    return res

unixTime = lambda y,m,d,h: int(time.mktime(datetime(y,m,d,h).timetuple()))

now = datetime.now()
y,m,d,h = now.year, now.month, now.day, now.hour

data = get_OHLC(unixTime(y,m,d,h),unixTime(y,m,d,h-1))

Time,Open,High,Low,Close = [],[],[],[],[]
for i in data:
    Time.append(i[0])
    Open.append(i[1])
    High.append(i[2])
    Low.append(i[3])
    Close.append(i[4])

pd.DataFrame({'open':Open, 'high':High, 'low':Low, 'close':Close}).to_csv('price.csv')bit2

os.getenv('PORT','8080')
os.getenv('IP','0.0.0.0')
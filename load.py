import pandas as pd
from redistimeseries.client import Client
from datetime import datetime

key = 'test'
rts = Client()
rts.delete(key)
rts.create(key, labels={'source': key})
df = pd.read_csv('a.csv')
for index, row in df.iterrows():
    d = datetime.strptime(row['ds'], '%Y-%m-%d') 
    millisec = round(d.timestamp()*1000)
    rts.add(key, millisec, row['y'])
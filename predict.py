import pandas as pd
from fbprophet import Prophet

def predict(x): 
    key = x['key']
    (yhat, yhat_lower, yhat_upper) = (f'yhat{{{key}}}', f'yhat_lower{{{key}}}', f'yhat_upper{{{key}}}')
    execute('DEL', yhat, yhat_lower, yhat_upper)
    execute('TS.CREATE', yhat, 'LABELS', 'source', key)
    execute('TS.CREATE', yhat_lower, 'LABELS', 'source', key)
    execute('TS.CREATE', yhat_upper, 'LABELS', 'source', key)
    
    r = execute('TS.RANGE',  key, '-', '+')
    print(len(r))
    df = pd.DataFrame.from_records(r,columns=['ds','y'])
    df['ds'] = pd.to_datetime(df['ds'],unit='ms')

    m = Prophet()
    m.fit(df) 
    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)
      
    for index, row in forecast[len(df):].iterrows():
        millisec = round(row['ds'].timestamp()*1000)
        execute('TS.MADD', yhat, millisec, row['yhat'], yhat_lower, millisec, row['yhat_lower'], yhat_upper, millisec, row['yhat_upper'])

gb = GearsBuilder()
gb.foreach(predict)
gb.run('test')


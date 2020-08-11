[![Actions Status](https://github.com/RedisGears/ProphetGears/workflows/CI/badge.svg)](https://github.com/RedisGears/ProphetGears/actions)

# ProphetGears

![RedisInsight screencase](Screencast.gif)


## Run

##### Install requirements
```bash
pip3 install -r requirements.txt
```

##### Build and run docker
```bash
docker build --tag redislabs/prophetgears:edge .
docker run -p 6379:6379 -it --rm redislabs/prophetgears:edge
```

##### Load raw data into RedisTimeSeries
```bash
python3 load.py 
```

##### Run RedisGears to produce predictions
```bash
gears-cli run --requirements ./predict_requirements.txt predict.py

```

##### Present results on RedisInsight
Install and run RedisInsight ([Docs](https://docs.redislabs.com/latest/ri/installing/)) and enter <http://127.0.0.1:8001/>

Add Redis instance using IP 127.0.0.1 and port 6379 and click the database.

From the sidebar choose RedisTimeSeries.

To see the original data enter query ```TS.RANGE test - +```.

To see original data and predictions enter query ```TS.MRANGE - + FILTER source=test```.

[![Actions Status](https://github.com/RedisGears/ProphetGears/workflows/CI/badge.svg)](https://github.com/RedisGears/ProphetGears/actions)

# ProphetGears

![RedisInsight screencase](Screencast.gif)


## Run
```bash
docker build --tag redislabs/prophetgears:edge .
docker run -p 6379:6379 -it --rm redislabs/prophetgears:edge
```

```bash
pip install -r requirements.txt
python3 load.py 
python3 gears.py --requirements ./predict_requirements.txt predict.py
```

```
./redisinsight-linux64-1.3.1
```


# ProphetGears

## Run
```bash
docker build --tag redislabs/prophetgears:edge .
docker run -p 6379:6379 -it --rm redislabs/prophetgears:edge

python3 load.py
python3 gears.py --requirements ./requirements.txt function.py
```

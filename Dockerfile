FROM redislabs/redismod:edge as redismod

ENV DEPS "gcc g++ build-essential python-pip"

# Set up a build environment
RUN set -ex;\
    deps="$DEPS";\
    apt-get update;\
    apt-get install -y --no-install-recommends $deps;
       
# ENV PYTHONPATH /usr/lib/redis/modules/deps/cpython/Lib
ENTRYPOINT ["redis-server"]
CMD [ "--logfile", "/var/log/redis-server.log", \
    "--loadmodule", "/usr/lib/redis/modules/redistimeseries.so", \
    "--loadmodule", "/var/opt/redislabs/lib/modules/redisgears.so", \
    "PythonHomeDir", "/opt/redislabs/lib/modules/python3"]

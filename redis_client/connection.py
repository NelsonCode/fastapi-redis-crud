from redis import Redis
from redis.exceptions import ConnectionError
from os import getenv


try:
    redis_client = Redis(
        host=getenv("REDIS_HOST"),
        port=getenv("REDIS_PORT"),
        password=getenv("REDIS_PASSWORD"),
        ssl=bool(getenv("REDIS_SSL"))
    )

    print("CONNECTED TO REDIS!")
except ConnectionError as e:
    print(e)

import aioredis
from config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC, KAFKA_TOPIC_REDIS
from aiokafka import AIOKafkaConsumer
import json
from fastapi import Depends, APIRouter, Query
import os


def is_simple(num: int) -> bool:
    """
    :param num: число
    :return: Является ли число простым
    """
    for i in range(2, num, 1):
        if not num % i:
            return False
    return True


def calc(num: int):
    """
    :param num: номер простого числа
    :return: простое число с номером num
    """
    count = 0
    ind = 2
    while count < num:
        ind += 1
        if is_simple(ind):
            count += 1
    return ind


async def consume():
    consumer = AIOKafkaConsumer(KAFKA_TOPIC_REDIS, loop=loop,
                                bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=os.environ['KAFKA_CONSUMER_GROUP'])
    await consumer.start()
    redis = aioredis.from_url("redis://redis")
    try:
        async for msg in consumer:
            print(f'Consumer msg: topic: {msg.topic},  partition: {msg.partition}, '
                  f'offset: {msg.partition}, key: {msg.key}')
            print(f'Consumer msg value: {json.loads(msg.value)}')
            num_json = json.loads(msg.value)
            num = num_json['value']
            cache = await redis.get(num)
            if cache is None:
                await redis.mset({num: calc(num)})
    finally:
        await consumer.stop()

router = APIRouter(
    prefix="/with_redis",
    responses={404: {"description": "Sorry Not found"}},
)


@router.get("/")
async def data(num: int = Query(None, title='num', description='num')):
    redis = aioredis.from_url("redis://redis")
    print(f'GET: {num}, {type(num)}')
    return await redis.get(num)  # Для ассинхронного запуска

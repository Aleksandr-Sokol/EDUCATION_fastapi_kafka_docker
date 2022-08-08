from fastapi import APIRouter
from schema import Message, UserSchema, NumSchema
from config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC, KAFKA_TOPIC_REDIS
from aiokafka import AIOKafkaProducer
import json

route = APIRouter()


@route.post('/simple_num')
async def send(num: NumSchema):
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        print(f'Sendding message with value: {num}')
        num_value_json = json.dumps(num.__dict__).encode('utf-8')
        await producer.send_and_wait(topic=KAFKA_TOPIC_REDIS, value=num_value_json)
    finally:
        await producer.stop()


@route.post('/user')
async def send(user: UserSchema):
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        print(f'Sendding message with value: {user}')
        value_json = json.dumps(user.__dict__).encode('utf-8')
        await producer.send_and_wait(topic=KAFKA_TOPIC, value=value_json)
    finally:
        await producer.stop()


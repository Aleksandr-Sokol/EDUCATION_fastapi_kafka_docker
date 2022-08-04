from config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer


async def consume():
    consumer = AIOKafkaConsumer(KAFKA_TOPIC, loop=loop,
                                bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=KAFKA_CONSUMER_GROUP)
    await consumer.start()
    try:
        async for msg in consumer:
            print(f'Consumer 1 msg: {msg}')
    finally:
        await consumer.stop()

consumer = AIOKafkaConsumer(KAFKA_TOPIC, loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=KAFKA_CONSUMER_GROUP)
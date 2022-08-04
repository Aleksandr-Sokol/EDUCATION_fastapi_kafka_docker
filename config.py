import asyncio

# env Variable
KAFKA_BOOTSTRAP_SERVERS = "0.0.0.0:9093"
KAFKA_TOPIC = "kafka_message"
KAFKA_CONSUMER_GROUP = "group-id"
loop = asyncio.get_event_loop()

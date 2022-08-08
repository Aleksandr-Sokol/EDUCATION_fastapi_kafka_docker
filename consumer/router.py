from config import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC
from aiokafka import AIOKafkaConsumer
import json
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from core.db import get_async_db
from crud.data_crud import UserDataCRUD
from schema import UserSchema, DataSchema
from core.db import AsyncSession, async_session


async def create_user(data: dict, db: AsyncSession = Depends(get_async_db)):
    print(f'POST: {db}, {type(db)}')
    data_crud = UserDataCRUD()
    return await data_crud.create(async_session(), **data)  # Для ассинхронного запуска


async def consume():
    consumer = AIOKafkaConsumer(KAFKA_TOPIC, loop=loop,
                                bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=KAFKA_CONSUMER_GROUP)
    await consumer.start()
    try:
        async for msg in consumer:
            print(f'Consumer msg: topic: {msg.topic},  partition: {msg.partition}, '
                  f'offset: {msg.partition}, key: {msg.key}')
            print(f'Consumer msg value: {json.loads(msg.value)}')
            await create_user(json.loads(msg.value))
    finally:
        await consumer.stop()

router = APIRouter(
    prefix="/user",
    responses={404: {"description": "Sorry Not found"}},
)


@router.get("/{data_id}", response_model=DataSchema)
async def data(data_id: int, db: AsyncSession = Depends(get_async_db)) -> DataSchema:
    print(f'GET: {db}, {type(db)}')
    data_crud = UserDataCRUD()
    return await data_crud.get(db, data_id)  # Для ассинхронного запуска
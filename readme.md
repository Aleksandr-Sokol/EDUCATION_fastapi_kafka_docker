# FastAPI + KAFKA + REDIS template

# Набор шаблонов для создания микросервиса с FastAPI + KAFKA + REDIS
##(Не является реальным проектом)
## docker-compose:
- zookeeper
- KAFKA
- kafdrop (для отслеживаия очередей через UI интерфейс)
- FastAPI (producer)
- FastAPI (consumer 1, регистрация пользователя)
- FastAPI (consumer 2, вычисление простых чисел с кешированием в redis)
- redis
- redis-commander

## Используемые технологии:
- FastAPI
- KAFKA (работа с топиками)
- REDIS
- Ассинхронный доступ к БД
- SQLite

## Реализованные микросервисы:
### (Взаимодействие осуществляется через брокер сообщений KAFKA)
- consumer 1 - чтение из своего топика информации о пользователе и сохранение в БД
- consumer 2 - чтение из своего топика номера простого числа. Поиск его в кеше redis, и если не найдено то вычисление
- producer - получение запросов и отправка их в соответствующие топики KAFKA

## Полезные ссылки
- [Как настроить SQLAlchemy, SQLModel и Alembic для асинхронной работы с FastAPI](https://habr.com/ru/post/580866/)
- https://fastapi.tiangolo.com/tutorial/
- https://stackoverflow.com/questions/63048825/how-to-upload-file-using-fastapi
- [Знакомство с FastAPI](https://habr.com/ru/post/488468/)
- https://habr.com/ru/post/513328/
- [Pydantic — умопомрачительная валидация данных на Python](https://www.youtube.com/watch?v=dOO3GmX6ukU&t=1s)
- [Pydantic Library Types](https://pydantic-docs.helpmanual.io/usage/types/)
- [fastapi databases async запросы](https://www.youtube.com/watch?v=CcsbCRzaxoE)
- https://www.starlette.io/events/

fastapi-microblog:
- https://www.youtube.com/watch?v=WkqM_SIXEuQ
- https://www.youtube.com/watch?v=AXYgXpHJhBA
- https://www.youtube.com/watch?v=eXj1gdDLKho
- https://github.com/DJWOMS/fastapi-microblog/
- https://www.youtube.com/watch?v=hmZe7gOrdSo&list=PLaED5GKTiQG8GW5Rv2hf3tRS-d9t9liUt&index=3
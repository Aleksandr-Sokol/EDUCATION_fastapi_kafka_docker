import sys
import asyncio
from fastapi import FastAPI
sys.path = ['', '..'] + sys.path[1:]
from router import consume
from router import router

app = FastAPI()

@app.get('/')
async def Home():
    return "welcome home consumer 1"

app.include_router(router)

asyncio.create_task(consume())

import sys

import asyncio
from fastapi import FastAPI
sys.path = ['', '..'] + sys.path[1:]
from router import consume

app = FastAPI()

@app.get('/')
async def Home():
    return "welcome home consumer 1"

asyncio.create_task(consume())

# @app.on_event("startup")
# async def startup_event():
#     """Start up event for FastAPI application."""
#     await consumer.start()
#
#
# @app.on_event("shutdown")
# async def shutdown_event():
#     """Shutdown event for FastAPI application."""
#     await consumer.stop()
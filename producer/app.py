import sys

from fastapi import FastAPI
sys.path = ['', '..'] + sys.path[1:]
from router import route


app = FastAPI()

@app.get('/')
async def Home():
    return "welcome home producer"

app.include_router(route)

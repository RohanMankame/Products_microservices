from typing import Union

from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:8000'],
    allow_methods=['*'],
    allow_headers=['*'],
)


redis = get_redis_connection(
    host="redis-12305.c305.ap-south-1-1.ec2.redns.redis-cloud.com",
    port=12305,
    password="uvxNKgVp1BbgGJSWgBZj38sMidb0YH7u",
    decode_responses=True
)

class Order(HashModel):
    product_id :str
    product_id: float
    fee: float
    total: float
    quantity:int
    status: str

    class Meta:
        database = redis

@app.post('/orders')
async def create(request: Request): # id, quantity
    body = await request.json()

    



import logging

from fastapi import FastAPI, Query, HTTPException
from starlette import status

from app.schemas import WriteData
from app.redis_client import get_redis_client

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Phone-Address Service",
    description="Сервис для хранения и получения адресов по номеру телефона с использованием Redis",
    version="1.0.0"
)
r = get_redis_client()


@app.get("/api/check")
def check_data(phone: str = Query(..., min_length=10, max_length=15)):
    """Получает адрес по номеру телефона из Redis."""
    address = r.get(phone)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"phone": phone, "address": address}


@app.post("/api/write")
def write_data(data: WriteData):
    """Записывает адрес и номер телефона в Redis."""
    logging.info(f"Saving address for phone: {data.phone}")
    r.set(data.phone, data.address, ex=3600)
    return {"message": "OK"}, status.HTTP_200_OK

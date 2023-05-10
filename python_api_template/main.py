import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# loggerを取得
logger: Logger = mylogger.get_logger("main")

app = FastAPI()


class Item(BaseModel):
    name: str
    price: int
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    logger.info("hello, world.")
    logger.info(mycredential.KEY)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

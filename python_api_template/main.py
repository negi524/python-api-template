import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential
from typing import Optional
from fastapi import FastAPI

# loggerを取得
logger: Logger = mylogger.get_logger("main")

app = FastAPI()


@app.get("/")
async def read_root():
    logger.info("hello, world.")
    logger.info(mycredential.KEY)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

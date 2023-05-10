import application_setting.my_logger as mylogger
from logging import Logger
import application_setting.my_credential as mycredential
from typing import Optional
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field

# loggerを取得
logger: Logger = mylogger.get_logger("main")

app = FastAPI()


class Item(BaseModel):
    name: str = Field(title="アイテム名")
    price: int = Field(title="アイテムの価格")
    is_offer: Optional[bool] = Field(default=None, title="オファー状態有無")


@app.get("/", tags=["sample"])
def read_root():
    """シンプルな{"Hello":"World"}のJSONを返却する

    Returns:
        dict: {"Hello":"World"}
    """
    logger.info("hello, world.")
    logger.info(mycredential.KEY)
    return {"Hello": "World"}


class ItemQuery(BaseModel):
    item_id: int = Field(title="アイテムID")
    q: str = Field(title="クエリ")

    class Config:
        schema_extra = {"example": {"item_id": 123, "q": "query"}}


@app.get("/items/{item_id}", tags=["item"], response_model=ItemQuery)
def read_item(
    item_id: int = Path(description="アイテムID"),
    q: Optional[str] = Query(default=None, description="クエリー"),
):
    """item_idとqをそのまま返却する

    Args:
        item_id (int): アイテムID
        q (Optional[str], optional): クエリ. Defaults to None.

    Returns:
        dict: クエリパラメータの値が格納されたJSON
    """
    return ItemQuery(item_id=item_id, q=q)


@app.put("/items/{item_id}", tags=["item"])
def update_item(
    item_id: int = Path(description="アイテムID"), item: Item = Body(description="アイテムの内容")
):
    return {"item_name": item.name, "item_id": item_id}

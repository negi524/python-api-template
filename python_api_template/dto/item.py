from typing import Optional
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(title="アイテム名")
    price: int = Field(title="アイテムの価格")
    is_offer: Optional[bool] = Field(default=None, title="オファー状態有無")


class ItemQuery(BaseModel):
    item_id: int = Field(title="アイテムID")
    q: str = Field(title="クエリ")

    class Config:
        schema_extra = {"example": {"item_id": 123, "q": "query"}}


class ItemResponse(BaseModel):
    item_name: str = Field(description="アイテム名")
    item_id: int = Field(description="アイテムID")

    class Config:
        schema_extra = {"example": {"item_name": "item name", "item_id": 1}}

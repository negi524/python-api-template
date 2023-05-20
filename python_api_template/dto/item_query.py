from pydantic import BaseModel, Field


class ItemQuery(BaseModel):
    item_id: int = Field(title="アイテムID")
    q: str = Field(title="クエリ")

    class Config:
        schema_extra = {"example": {"item_id": 123, "q": "query"}}

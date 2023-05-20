from pydantic import BaseModel, Field


class ItemResponse(BaseModel):
    item_name: str = Field(description="アイテム名")
    item_id: int = Field(description="アイテムID")

    class Config:
        schema_extra = {"example": {"item_name": "item name", "item_id": 1}}

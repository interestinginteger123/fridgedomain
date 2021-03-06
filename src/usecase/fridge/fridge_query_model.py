from typing import cast

from pydantic import BaseModel, Field

from src.domain.fridge import Fridge


class FridgeReadModel(BaseModel):
    """FridgeReadModel represents data structure as a read model."""

    id: str = Field(example="Fridge1")
    shelves: int = Field(example=1)
    created_at: int = Field(example=1136214245000)
    updated_at: int = Field(example=1136214245000)

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(fridge: Fridge) -> "FridgeReadModel":
        return FridgeReadModel(
            id=fridge.id,
            shelves=fridge.shelves,
            created_at=cast(int, fridge.created_at),
            updated_at=cast(int, fridge.updated_at)
        )

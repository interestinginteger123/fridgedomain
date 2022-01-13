from pydantic import BaseModel, Field


class FridgeCreateModel(BaseModel):
    """FridgeCreateModel represents a write model to create a fridge."""

    shelves: int = Field(example=5)


class FridgeUpdateModel(BaseModel):
    """FridgeUpdateModel represents a write model to update the number shelves in a fridge."""

    shelves: int = Field(
        example=5
    )
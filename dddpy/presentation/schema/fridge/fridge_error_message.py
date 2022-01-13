from pydantic import BaseModel, Field

from dddpy.domain.fridge import (
    FridgeNotFoundError,
    ShelvesNotFoundError
)


class ErrorMessageFridgeNotFound(BaseModel):
    detail: str = Field(example=FridgeNotFoundError.message)


class ErrorMessageShelvesNotFound(BaseModel):
    detail: str = Field(example=ShelvesNotFoundError.message)
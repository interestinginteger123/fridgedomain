from datetime import datetime
from typing import Union

from sqlalchemy import Column, Integer, String

from src.domain.fridge import Fridge
from src.infrastructure.sql.database import Base
from src.usecase.fridge import FridgeReadModel


def unixtimestamp() -> int:
    return int(datetime.now().timestamp() * 1000)


class FridgeDTO(Base):
    """FridgeDTO is a data transfer object associated with a Fridge entity."""

    __tablename__ = "fridge"
    id: Union[str, Column] = Column(String, primary_key=True, autoincrement=False)
    shelves: Union[int, Column] = Column(Integer, nullable=False)
    created_at: Union[int, Column] = Column(Integer, index=True, nullable=False)
    updated_at: Union[int, Column] = Column(Integer, index=True, nullable=False)

    def to_entity(self) -> Fridge:
        return Fridge(
            id=self.id,
            shelves=self.shelves,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def to_read_model(self) -> FridgeReadModel:
        return FridgeReadModel(
            id=self.id,
            shelves=self.shelves,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(fridge: Fridge) -> "FridgeDTO":
        now = unixtimestamp()
        return FridgeDTO(
            id=fridge.id,
            shelves=fridge.shelves,
            created_at=now,
            updated_at=now,
        )

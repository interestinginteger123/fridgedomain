from abc import ABC, abstractmethod
from typing import List, Optional

from .fridge_query_model import FridgeReadModel


class FridgeQueryService(ABC):
    """FridgeQueryService defines a query service interface related Fridge entity."""

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[FridgeReadModel]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[FridgeReadModel]:
        raise NotImplementedError
from abc import ABC, abstractmethod
from typing import Optional

from src.domain.fridge import Fridge


class FridgeRepository(ABC):
    """FridgeRepository defines a repository interface for fridge entity."""

    @abstractmethod
    def create(self, fridge: Fridge) -> Optional[Fridge]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Fridge]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str) -> Optional[Fridge]:
        raise NotImplementedError
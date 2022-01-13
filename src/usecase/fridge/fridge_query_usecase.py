from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.fridge import FridgeNotFoundError, FridgeNotFoundError

from .fridge_query_model import FridgeReadModel
from .fridge_query_service import FridgeQueryService


class FridgeQueryUseCase(ABC):
    """FridgeQueryUseCase defines a query usecase interface related Fridge entity."""

    @abstractmethod
    def fetch_fridge_by_id(self, id: str) -> Optional[FridgeReadModel]:
        raise NotImplementedError

    @abstractmethod
    def fetch_fridges(self) -> List[FridgeReadModel]:
        raise NotImplementedError


class FridgeQueryUseCaseImpl(FridgeQueryUseCase):
    """FridgeQueryUseCaseImpl implements a query usecases related Fridge entity."""

    def __init__(self, fridge_query_service: FridgeQueryService):
        self.fridge_query_service: FridgeQueryService = fridge_query_service

    def fetch_fridge_by_id(self, id: str) -> Optional[FridgeReadModel]:
        try:
            fridge = self.fridge_query_service.find_by_id(id)
            if fridge is None:
                raise FridgeNotFoundError
        except:
            raise

        return fridge

    def fetch_fridges(self) -> List[FridgeReadModel]:
        try:
            books = self.fridge_query_service.find_all()
        except:
            raise

        return books

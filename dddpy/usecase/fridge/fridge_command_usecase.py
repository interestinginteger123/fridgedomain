import uuid

from abc import ABC, abstractmethod
from typing import Optional, cast

from dddpy.domain.fridge import (
    Fridge,
    FridgeRepository,
    FridgeNotFoundError,
    FridgeAlreadyExistsError
)

from .fridge_command_model import FridgeCreateModel, FridgeUpdateModel
from .fridge_query_model import FridgeReadModel


class FridgeCommandUseCaseUnitOfWork(ABC):
    """FridgeCommandUseCaseUnitOfWork defines an interface based on Unit of Work pattern."""

    fridge_repository: FridgeRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class FridgeCommandUseCase(ABC):
    """FridgeCommandUseCase defines a command usecase interface related Book entity."""

    @abstractmethod
    def create_fridge(self, data: FridgeCreateModel) -> Optional[FridgeReadModel]:
        raise NotImplementedError

    @abstractmethod
    def update_fridge(self, id: str, data: FridgeUpdateModel) -> Optional[FridgeReadModel]:
        raise NotImplementedError

    @abstractmethod
    def delete_fridge_by_id(self, id: str):
        raise NotImplementedError


class FridgeCommandUseCaseImpl(FridgeCommandUseCase):
    """FridgeCommandUseCaseImpl implements a command usecases related Fridge entity."""

    def __init__(
        self,
        uow: FridgeCommandUseCaseUnitOfWork,
    ):
        self.uow: FridgeCommandUseCaseUnitOfWork = uow

    def create_fridge(self, data: FridgeCreateModel) -> Optional[FridgeReadModel]:
        try:
            _uuid = str(uuid.uuid4())
            fridge = Fridge(id=_uuid, shelves=1)
            self.uow.fridge_repository.create(fridge)
            self.uow.commit()

            created_fridge = self.uow.fridge_repository.find_by_id(_uuid)
        except:
            self.uow.rollback()
            raise

        return FridgeReadModel.from_entity(cast(Fridge, created_fridge))

    def update_fridge(self, id: str, data: FridgeUpdateModel) -> Optional[FridgeReadModel]:
        try:
            existing_fridge = self.uow.fridge_repository.find_by_id(id)
            if existing_fridge is None:
                raise FridgeNotFoundError

            fridge = Fridge(
                id=id,
                shelves=existing_fridge.shelves
            )

            self.uow.fridge_repository.update(fridge)

            updated_fridge = self.uow.fridge_repository.find_by_id(fridge.id)

            self.uow.commit()
        except:
            self.uow.rollback()
            raise

        return FridgeReadModel.from_entity(cast(Fridge, updated_fridge))

    def delete_fridge_by_id(self, id: str):
        try:
            existing_fridge = self.uow.fridge_repository.find_by_id(id)
            if existing_fridge is None:
                raise FridgeNotFoundError

            self.uow.fridge_repository.delete_by_id(id)

            self.uow.commit()
        except:
            self.uow.rollback()
            raise

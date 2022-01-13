from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from src.domain.fridge import Fridge, FridgeRepository
from src.usecase.fridge import FridgeCommandUseCaseUnitOfWork

from .fridge_dto import FridgeDTO


class FridgeRepositoryImpl(FridgeRepository):
    """FridgeRepositoryImpl implements CRUD operations related Fridge entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> Optional[Fridge]:
        try:
            fridge_dto = self.session.query(FridgeDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return fridge_dto.to_entity()

    def create(self, fridge: Fridge):
        fridge_dto = FridgeDTO.from_entity(fridge)
        try:
            self.session.add(fridge_dto)
        except:
            raise

    def update(self, fridge: Fridge):
        fridge_dto = FridgeDTO.from_entity(fridge)
        try:
            _fridge = self.session.query(FridgeDTO).filter_by(id=fridge_dto.id).one()
            _fridge.shelves = fridge_dto.shelves
            _fridge.updated_at = fridge_dto.updated_at
        except:
            raise

    def delete_by_id(self, id: str):
        try:
            self.session.query(FridgeDTO).filter_by(id=id).delete()
        except:
            raise


class FridgeCommandUseCaseUnitOfWorkImpl(FridgeCommandUseCaseUnitOfWork):
    def __init__(
        self,
        session: Session,
        fridge_repository: FridgeRepository,
    ):
        self.session: Session = session
        self.fridge_repository: FridgeRepository = fridge_repository

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

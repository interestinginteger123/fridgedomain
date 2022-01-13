from typing import List, Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from dddpy.usecase.fridge import FridgeQueryService, FridgeReadModel

from .fridge_dto import FridgeDTO


class FridgeQueryServiceImpl(FridgeQueryService):
    """FridgeQueryServiceImpl implements READ operations related Fridge entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> Optional[FridgeReadModel]:
        try:
            fridge_dto = self.session.query(FridgeDTO).filter_by(id=id).one()
        except NoResultFound:
            return None
        except:
            raise

        return fridge_dto.to_read_model()

    def find_all(self) -> List[FridgeReadModel]:
        try:
            fridge_dtos = (
                self.session.query(FridgeDTO)
                .order_by(FridgeDTO.updated_at)
                .limit(100)
                .all()
            )
        except:
            raise

        if len(fridge_dtos) == 0:
            return []

        return list(map(lambda fridge_dto: fridge_dto.to_read_model(), fridge_dtos))

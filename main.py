import logging
from logging import config
from typing import Iterator, List

from sqlalchemy.orm.session import Session

from dddpy.domain.fridge import (
    FridgeNotFoundError,
    FridgeAlreadyExistsError,
    ShelvesNotFoundError,
    FridgeRepository
)

from dddpy.infrastructure.sql.fridge import (
    FridgeCommandUseCaseUnitOfWorkImpl,
    FridgeQueryServiceImpl,
    FridgeRepositoryImpl,
)

from dddpy.infrastructure.sql.database import SessionLocal, create_tables
from dddpy.presentation.schema.fridge.fridge_error_message import (
    ErrorMessageShelvesNotFound,
    ErrorMessageFridgeNotFound,
)


from dddpy.presentation.schema.fridge.fridge_error_message import (
    FridgeNotFoundError,
    ShelvesNotFoundError
)

from dddpy.usecase.fridge import (
    FridgeCommandUseCase,
    FridgeCommandUseCaseImpl,
    FridgeCommandUseCaseUnitOfWork,
    FridgeCreateModel,
    FridgeQueryService,
    FridgeQueryUseCase,
    FridgeQueryUseCaseImpl,
    FridgeReadModel,
    FridgeUpdateModel,
)

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

create_tables()

def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def fridge_query_usecase(session: Session = get_session()) -> FridgeQueryUseCase:
    fridge_query_service: FridgeQueryService = FridgeQueryServiceImpl(session)
    return FridgeQueryUseCaseImpl(fridge_query_service)


def fridge_command_usecase(session: Session = get_session()) -> FridgeCommandUseCase:
    fridge_repository: FridgeRepository = FridgeRepositoryImpl(session)
    uow: FridgeCommandUseCaseUnitOfWork = FridgeCommandUseCaseUnitOfWorkImpl(
        session, fridge_repository=fridge_repository
    )
    return FridgeCommandUseCaseImpl(uow)

def create_fridge(
    data: FridgeCreateModel,
    fridge_command_usecase: FridgeCommandUseCase = fridge_command_usecase(),
):
    try:
        fridge = fridge_command_usecase.create_fridge(data)
    except FridgeAlreadyExistsError as e:
        print(e.message)
    return fridge


if __name__ == "__main__":
    fridge = {'shelves':5}
    
    create_fridge(fridge)
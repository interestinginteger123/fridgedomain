import pytest
from src.domain import fridge

from src.domain.fridge import Fridge
from src.infrastructure.sql.fridge import FridgeDTO


class TestFridgeDTO:
    def test_to_read_model_should_create_entity_instance(self):
        fridge_dto = FridgeDTO(
            id="fridge_01",
            shelves=3,
            created_at=1614007224642,
            updated_at=1614007224642,
        )

        fridge = fridge_dto.to_read_model()

        assert fridge.id == "fridge_01"
        assert fridge.shelves == 3

    def test_to_entity_should_create_entity_instance(self):
        fridge_dto = FridgeDTO(
            id="fridge_01",
            shelves=5,
            created_at=1614007224642,
            updated_at=1614007224642,
        )

        fridge = fridge_dto.to_entity()

        assert fridge.id == "fridge_01"
        assert fridge.shelves == 5


    def test_from_entity_should_create_dto_instance(self):
        fridge = Fridge(
            id="fridge_01",
            shelves=5,
            created_at=1614007224642,
            updated_at=1614007224642
        )

        fridge_dto = FridgeDTO.from_entity(fridge)

        assert fridge_dto.id == "fridge_01"
        assert fridge_dto.shelves == 5


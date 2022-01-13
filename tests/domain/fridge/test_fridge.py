import pytest

from src.domain.fridge import Fridge


class TestFridge:
    def test_constructor_should_create_instance(self):
        fridge = Fridge(
            id="Fridge01",
            shelves=5
        )

        assert fridge.id == "Fridge01"
        assert fridge.shelves == 5

    def test_fridge_entity_should_be_identified_by_id(self):
        fridge_1 = Fridge(
            id="Fridge01",
            shelves=5,
        )

        fridge_2 = Fridge(
            id="Fridge01",
            shelves=6        
        )

        fridge_3 = Fridge(
            id="Fridge03",
            shelves=4
        )

        assert fridge_1 == fridge_2
        assert fridge_1 != fridge_3   
from typing import Optional

class Food:
    """Food represents food in a fridge"""
    def __init__(
        self,
        id: str,
        type: str,
        shelf: int
    ):
        self.id: str = id
        self.shelf: int = shelf
    
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Food):
            return self.id == o.id
        return False

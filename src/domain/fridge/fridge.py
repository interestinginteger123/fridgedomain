from typing import Optional


class Fridge:
    """Fridge represents your collection of shelves as an entity."""

    def __init__(
        self,
        id: str,
        shelves: int,
        created_at: Optional[int] = None,
        updated_at: Optional[int] = None
    ):
        self.id: str = id
        self.shelves: int = shelves
        self.created_at: Optional[int] = created_at
        self.updated_at: Optional[int] = updated_at
    
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Fridge):
            return self.id == o.id

        return False
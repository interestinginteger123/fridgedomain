class FridgeNotFoundError(Exception):
    message = "The fridge does not exist."

    def __str__(self):
        return FridgeNotFoundError.message


class ShelvesNotFoundError(Exception):
    message = "No shelves were found."

    def __str__(self):
        return ShelvesNotFoundError.message


class FridgeAlreadyExistsError(Exception):
    message = "The Fridge already exists."

    def __str__(self):
        return FridgeAlreadyExistsError.message
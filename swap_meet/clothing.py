from .item import Item


class Clothing(Item):
    def __str__(self):
        return "The finest clothing you could wear."

    def __init__(self, condition=None):
        super().__init__(category="Clothing", condition=condition)

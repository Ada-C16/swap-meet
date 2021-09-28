from .item import Item


class Decor(Item):
    def __str__(self) -> str:
        return "Something to decorate your space."

    def __init__(self, category="Decor", condition=None):
        super().__init__(category, condition)

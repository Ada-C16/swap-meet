from .item import Item


class Decor(Item):
    def __str__(self):
        return "Something to decorate your space."

    def __init__(self, condition=None):
        super().__init__(category="Decor", condition=condition)

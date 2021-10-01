from .item import Item


class Decor(Item):
    def __init__(self, name="", condition=0, age=None):
        super().__init__(name, condition, age, category="Decor")

    def __str__(self):
        return "Something to decorate your space."

from .item import Item

class Decor(Item):
    def __init__(self, name="", condition=0):
        super().__init__(name, condition, category = "Decor")

    def __str__(self):
        return "Something to decorate your space."

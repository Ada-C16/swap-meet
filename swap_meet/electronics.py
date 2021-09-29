from .item import Item

class Electronics(Item):
    def __init__(self, category = "Electronics", condition = None, age = None):
        super().__init__(category, condition, age)

    def __str__(self):
        return "A gadget full of buttons and secrets."

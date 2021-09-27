from .item import Item

class Electronics(Item):
    def __init__(self, category = "Electronics", condition = None):
        super().__init__(category, condition)
        self.category = category
    def __str__(self):
        return "A gadget full of buttons and secrets."

from .item import Item

class Clothing(Item):
    def __init__(self, category=None, condition = 0):
        super().__init__(category="Clothing", condition=condition)
        self.category = "Clothing"
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."
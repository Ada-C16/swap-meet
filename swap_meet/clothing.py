from .item import Item

class Clothing(Item):
    def __init__(self, condition = 0, category = "Clothing"):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."

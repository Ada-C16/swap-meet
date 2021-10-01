from swap_meet.item import Item


from .item import Item


class Clothing(Item):
    def __init__(self, condition=0, age=None):
        super().__init__(condition, age, category="Clothing")

    def __str__(self):
        return "The finest clothing you could wear."

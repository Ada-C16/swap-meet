from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition = None):
        self.category = "Decor"
        self.condition = condition if condition is not None else 0

    def __str__(self):
        return "Something to decorate your space."

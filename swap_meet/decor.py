from swap_meet.item import Item

class Decor(Item):
    pass
    def __init__(self, condition = 0):
        category = "Decor"
        self.category = category
        self.condition = condition
    def __str__(cls):
        return "Something to decorate your space."  
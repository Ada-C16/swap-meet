from swap_meet.item import Item

class Electronics(Item):
    pass
    def __init__(self, category = "Electronics", condition = None, age = None):
        super().__init__(category, condition, age)
    def __str__(cls):
        return "A gadget full of buttons and secrets."

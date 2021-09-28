from swap_meet.item import Item

class Electronics(Item):
    pass
    def __init__(self, condition = 0):
        category = "Electronics"
        self.category = category
        self.condition = condition
    def __str__(cls):
        return "A gadget full of buttons and secrets."

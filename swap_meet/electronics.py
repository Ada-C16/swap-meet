from .item import Item

class Electronics(Item):
    def __init__(self, name="", condition=0):
        super().__init__(name, condition, category = "Electronics")

    def __str__(self):
        return "A gadget full of buttons and secrets."

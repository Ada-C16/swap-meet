from .item import Item


class Electronics(Item):
    def __init__(self, condition=0, age=None):
        super().__init__(condition, age=None, category="Electronics")

    def __str__(self):
        return "A gadget full of buttons and secrets."

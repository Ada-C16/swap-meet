from .item import Item


class Electronics(Item):
    def __str__(self) -> str:
        return "A gadget full of buttons and secrets."

    def __init__(self, category="Electronics", condition=None):
        super().__init__(category, condition)

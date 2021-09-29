from .item import Item

class Electronics(Item):
    """class Electronics is a child to parent class Item"""

    def __init__(self, condition = None):
        """Assigns category of instance to Electronics and passes in the condition as none"""
        super().__init__(category = "Electronics", condition = condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
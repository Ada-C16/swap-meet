from .item import Item

class Decor(Item):
    """class Decor is a child to parent class Item"""

    def __init__(self, condition = None):
        """Assigns category of instance to Decor and passes in the condition as none"""
        super().__init__(category = "Decor", condition = condition)

    def __str__(self):
        return "Something to decorate your space."

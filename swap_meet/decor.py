from .item import Item

class Decor(Item):
    """
    Class Decor, subclass of class Item
    """ 
    # class constructor method & super method
    def __init__(self, condition=0):
        super().__init__(condition = condition)
        self.category = "Decor"

    # stringify instances of class Decor
    def __str__(self):
        return "Something to decorate your space."

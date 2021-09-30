from .item import Item

class Clothing(Item):
    """
    Class Clothing, subclass of class Item
    """ 
    # class constructor method & super method
    def __init__(self, condition=0):
        super().__init__(condition=condition)
        self.category = "Clothing"

    # stringify instances of class Clothing
    def __str__(self):
        return "The finest clothing you could wear."



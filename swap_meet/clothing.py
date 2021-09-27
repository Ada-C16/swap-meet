from .item import Item

class Clothing(Item):
    # new init method with new paramaters
    def __init__(self, category = "Clothing", condition = None):
        # call superclass' constructor
        super().__init__(category, condition)

    def __str__(self):
        return "The finest clothing you could wear."

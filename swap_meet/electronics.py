from .item import Item

class Electronics(Item):
    """
    Class Electronics, subclass of class Item
    """   
    # class constructor method & super method 
    def __init__(self, condition=0):
        super().__init__(condition = condition)
        self.category = "Electronics"

    # stringify instances of class Electronics
    def __str__(self):
        return "A gadget full of buttons and secrets."

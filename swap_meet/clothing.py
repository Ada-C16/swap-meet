from .item import Item

class Clothing(Item):
    """class Clothin is a child to parent class Item"""

    def __init__(self, condition = None):
        """Assigns category of instance to Clothing and passes in the condition as none"""
        super().__init__(category = "Clothing", condition = condition)
    
    def __str__(self):
        return "The finest clothing you could wear."
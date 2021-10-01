from .item import Item

class Clothing(Item):
    def __init__(self, category = "Clothing", condition=0):
        # bc I'm inheriting Item category I have to use super()
        super().__init__(category, condition=condition)
    def __str__(self):  
        return ("The finest clothing you could wear.")


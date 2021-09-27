from .item import Item
class Decor(Item):
    def __str__(self):
        return "Something to decorate your space."

    def __init__(self,  condition=0):
        #super().__init__(Item, self)
        self.condition = condition
        self.category = "Decor"
    

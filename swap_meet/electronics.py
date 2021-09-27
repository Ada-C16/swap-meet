from .item import Item
class Electronics(Item):
    def __str__(self):
        return "A gadget full of buttons and secrets."
    
    def __init__(self,  condition=0):
        #super().__init__(Item, self)
        self.condition = condition
        self.category = "Electronics"
     
from .item import Item

class Decor(Item):

    # ********* Wave 5 **********
    
    def __init__(self, condition=0):
        super().__init__(category="Decor", condition=condition)
    
    def __str__(self):
        return "Something to decorate your space."

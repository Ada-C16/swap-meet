from .item import Item

class Decor(Item):
    def __init__(self):
        super().__init__(self, condition=0)
        self.category = "Decor"
    
    def __str__(self):
        return f"Something to decorate your space."

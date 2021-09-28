from .item import Item

class Decor(Item):
    def __init__(self, category = "Decor", condition = None, age = None):
        super().__init__(category, condition, age)
    
    def condition_description(self):
        return f"This item's condition is {self.condition}"
    
    def __str__(self):
        return "Something to decorate your space."

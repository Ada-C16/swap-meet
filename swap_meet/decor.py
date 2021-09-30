from swap_meet.item import Item

class Decor(Item):
    pass
    def __init__(self, category = "Decor", condition = None, age = None):
        super().__init__(category, condition, age)
    def __str__(cls):
        return "Something to decorate your space."

   

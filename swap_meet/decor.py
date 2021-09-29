from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition = 0.0):
        super().__init__(condition, category = "Decor")


        # self.category = category
        # self.condition = condition
    

    def __str__(self):
        return "Something to decorate your space."

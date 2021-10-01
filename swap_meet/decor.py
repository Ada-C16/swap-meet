
from swap_meet.item import Item

class Decor(Item):
    def __init__ (self, condition = 0 ):
        super().__init__(condition = 0, category = "")
        self.category = 'Decor'
        if condition :
            self.condition = condition
        else:
            self.inventory = 0

    def __str__(self):
        return "Something to decorate your space."

    # def condition_description(self):
    #     decor_description = super().condition_description()
    #     return decor_description
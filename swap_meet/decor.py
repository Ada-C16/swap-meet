from swap_meet.item import Item
class Decor(Item):
    
    def __init__(self, category = "Decor", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Something to decorate your space."
    
    def condition_description(self):
        if self.condition == 0:
            return "This sucks."
        elif self.condition == 1:
            return "Eh, you can do better."
        elif self.condition == 2:
            return "This isn't the worst thing on Earth."
        elif self.condition == 3:
            return "This is almost average."
        elif self.condition == 4:
            return "This is pretty good quality."
        elif self.condition == 5:
            return "Nothing tops this!"
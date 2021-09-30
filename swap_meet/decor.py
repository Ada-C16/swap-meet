from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category="Decor", age=-1, condition=0):
        super().__init__(category, age, condition)

    def __str__(self):
        return "Something to decorate your space." 

from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category = None, condition = None, age = None):
        super().__init__(category, condition, age)
        self.category = "Clothing"

    def __str__(self):
        return "The finest clothing you could wear."

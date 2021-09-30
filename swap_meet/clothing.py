from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category = "Clothing", condition = None, age = None):
        super().__init__(category, condition, age)
    def __str__(cls):
        return "The finest clothing you could wear." 
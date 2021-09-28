from swap_meet.item import Item

class Clothing(Item):
    pass
    def __init__(self, condition = 0):
        category = "Clothing"
        self.category = category 
        self.condition = condition
    def __str__(cls):
        return "The finest clothing you could wear."
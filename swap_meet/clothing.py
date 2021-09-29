from swap_meet.item import Item

class Clothing(Item):
    def __init__(self):
        super().__init__(self, condition=0)
        self.category = "Clothing"

    def __str__(self):
        return "The finest clothing you could wear."



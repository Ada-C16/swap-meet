from swap_meet.item import Item

class Clothing(Item):
    # Want to use attributes from Item Class (keep condition as is)
    # But want to declare category as Clothing (modify)
    def __init__(self, category = None, condition = None):
        super().__init__(category, condition)
        self.category = "Clothing"

    def __str__(self):
        return "The finest clothing you could wear."

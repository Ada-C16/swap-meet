from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = 0, age = 0):
        """
        is a subclass of item, defines its own category attribute 
        and condition, inherits method for condition description
        from parent
        """
        #super().__init__()
        self.category = "Clothing"
        self.condition = condition
        self.age = 0

    def __str__(self):
        return "The finest clothing you could wear."



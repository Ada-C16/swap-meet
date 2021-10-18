from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition = 0, age = 0):
        """
        is a subclass of item, defines its own category attribute 
        and condition, inherits method for condition description
        from parent
        """
        self.category = "Decor"
        self.condition = condition 
    def __str__(self):
        return "Something to decorate your space."

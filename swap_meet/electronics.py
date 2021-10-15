from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition = 0, age = 0):
        """
        is a subclass of item, defines its own category attribute 
        and condition, inherits method for condition description
        from parent
        """
        self.category = "Electronics"
        self.condition = condition
        self.age = age

    def __str__(self):
        return "A gadget full of buttons and secrets."

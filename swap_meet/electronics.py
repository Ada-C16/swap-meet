from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category = "", condition = 0):
        super().__init__(category = "", condition = 0)
        self.condition = condition
        self.category = "Electronics"

    def __str__(self):
        return "A gadget full of buttons and secrets."

        
       


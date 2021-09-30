from swap_meet.item import Item

class Electronics(Item):
    def __init__(self,age=0, condition = 0):
        super().__init__(age,condition, category = "Electronics")
        
    def __str__(self):
        return "A gadget full of buttons and secrets."

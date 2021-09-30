from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category="Electronics", age=-1, condition=0):
        super().__init__(category, age, condition)
    
    def __str__(self):
        return "A gadget full of buttons and secrets."

from .item import Item

class Electronics(Item):
    def __init__(self):
        super().__init__(self, condition=0)
        self.category = "Electronics"
    
    def __str__(self):
        return f"A gadget full of buttons and secrets."

from .item import Item

class Electronics(Item):
    def __init__(self, category = 'Electronics', condition = 0.0, age = 0):
        super().__init__(category, condition, age)
        

    def __str__(self, description = 'A gadget full of buttons and secrets.'):
        return super().__str__(description)

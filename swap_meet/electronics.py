from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category="Electronics", condition=0.0):
        super().__init__(category=category, condition=condition)
        self.category = category

    def __str__(self):
        return "A gadget full of buttons and secrets."

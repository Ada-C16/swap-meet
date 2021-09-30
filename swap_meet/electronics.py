from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category = "Electronics", condition = 0):
        self.category = category
        self.condition = condition

        #super().__init__(category = "Clothing", conditon = condition)

        #super().condition_description()

    def __str__(self):
        return "A gadget full of buttons and secrets."


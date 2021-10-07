from .item import Item

class Electronics(Item):
    def __init__(self, condition = 0, age = 0):
        super().__init__()
        self.category = "Electronics"
        self.condition = condition if condition else condition == 0
        self.age = age if age else age == 0

    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        return super().condition_description()

    def age_description(self):
        return super().age_description()
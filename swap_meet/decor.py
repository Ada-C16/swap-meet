from .item import Item

class Decor(Item):
    def __init__(self, condition = 0, age = 0):
        super().__init__()
        self.category = "Decor"
        self.condition = condition if condition else condition is 0
        self.age = age if age else age is 0

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        return super().condition_description()

    def age_description(self):
        return super().age_description()
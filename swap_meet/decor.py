from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category = "Decor", condition = 0, age = 0):
        super().__init__(category, condition, age)
    def __str__(self):
        return "Something to decorate your space."
    def condition_description(self):
        condition = super().condition_description()
        return condition
    def age_description(self):
        age = super().age_description()
        return age

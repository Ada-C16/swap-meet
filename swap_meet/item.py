
class Item:
    def __init__(self, category="", condition=0, age=None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition = self.condition

        if condition == 0:
            condition_description = "Some garbage is OK"
        elif condition == 1:
            condition_description = "kind of embarassing, but you can probably wait till payday to replace"
        elif condition == 2:
            condition_description = "woof, it might be time for a new one girl..."
        elif condition == 3:
            condition_description = "she's fine"
        elif condition == 4:
            condition_description = "better than some"
        elif condition == 5:
            condition_description = "wow"

        return condition_description

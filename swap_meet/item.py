class Item:
    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return f"Category: {self.category}, Condition: {self.condition_description()}, Age: {self.age}"

    def condition_description(self):
        if self.condition == 5:
            return "New"
        elif self.condition >= 4:
            return "Like New"
        elif self.condition >= 3:
            return "Good Condition"
        elif self.condition >= 2:
            return "Fair Condition"
        elif self.condition >= 1:
            return "Poor Condition"
        else:
            return "Junk"

item = Item()
print(item)
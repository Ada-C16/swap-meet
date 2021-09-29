class Item:
    def __init__(self, category = "", condition = None, age = None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        return f"This item's condition is {self.condition}"
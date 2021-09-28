class Clothing:
    def __init__(self, category = "Clothing", condition = None):
        self.category = category
        self.condition = condition

    def condition_description(self):
        return f"This item's condition is {self.condition}"

    def __str__(self):
        return "The finest clothing you could wear."

class Decor:
    def __init__(self, category = "Decor", condition = None):
        self.category = category
        self.condition = condition
    
    def condition_description(self):
        return f"This item's condition is {self.condition}"
    
    def __str__(self):
        return "Something to decorate your space."

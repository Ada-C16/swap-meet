class Electronics:
    def __init__(self, category = "Electronics", condition = None):
        self.category = category
        self.condition = condition

    def condition_description(self):
        return f"This item's condition is {self.condition}"

    def __str__(self):
        return "A gadget full of buttons and secrets."

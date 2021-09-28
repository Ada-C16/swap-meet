class Item:
    def __init__(self, category = None, condition = None):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
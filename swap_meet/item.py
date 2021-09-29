class Item:
    def __init__(self, category=None):
        self.category = "" if category is None else category

    def __str__(self):
        return f"Hello World!"
        
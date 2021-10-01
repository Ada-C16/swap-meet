class Item:
    def __init__(self, category=""):
        self.category = category

    def __str__(self):
        if self.category == "":
            return "Hello World!"
        else:
            return self.category

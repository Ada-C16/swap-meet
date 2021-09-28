class Item:
    def __init__(self, category=None):
        if category:
            self.category = category
        else: 
            self.category = ""

    def __str__(self):
        return "Hello World!"

    
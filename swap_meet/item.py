from .clothing import Clothing
from .decor import Decor
from .electronics

class Item:
    def __init__(self, category = None, condition = None):
        if not category:
            category = ""
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
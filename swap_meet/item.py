from functools import total_ordering


@total_ordering
class Item:
    def __str__(self):
        return "Hello World!"

    def __lt__(self, other):
        return self.condition < other.condition

    def __init__(self, category=None, condition=None):
        self.category = category or ""
        self.condition = condition or 0.0

    def condition_description(self):
        descriptions = (
            "What",
            "Notions of form and substance",
            "Can't tell what's going on here",
            "Pretty sure it's a thing",
            "An object",
            "This is definitely an item",
        )
        return descriptions[int(self.condition)]

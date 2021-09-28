CONDITIONS_DICTIONARY = {
    0: "terrible",
    1: "pretty bad",
    2: "not great",
    3: "meh",
    4: "nice",
    5: "brand new",
}

class Item:
    
    def __init__(self, category="", condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        return CONDITIONS_DICTIONARY[self.condition]


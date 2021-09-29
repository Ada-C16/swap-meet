class Item:
    def __init__(self, category = "", condition = None, age = None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if 0 <= self.condition and self.condition < 1:
            return "Cast this into Mordor. Immediately."
        elif 1 <= self.condition and self.condition < 2:
            return "An item only a mother could love."
        elif 2 <= self.condition and  self.condition < 3:
            return "Hopefully we can repurpose this."
        elif 3 <= self.condition and self.condition < 4:
            return "Nothing to write home about, but somewhat useful."
        elif 4 <= self.condition and self.condition < 5:
            return "Butter my rump and call me toast, this is fantastic."
        else:
            return "*chef's kiss*"
class Item:
    def __init__(self, category="", condition = 0):
        self.category = category
        self.condition = float(condition)

    def __str__(self):
        if self.category == "":
            return "Hello World!"
        else:
            return self.category
    
    def condition_description(self): 
        if 0 <= self.condition < 1:
            return "Throw it out!"
        elif 1 <= self.condition < 2:
            return "Heavily used"
        elif 2 <= self.condition < 3:
            return "Used, but still ok"
        elif 3 <= self.condition < 4:
            return "Decent condition"
        elif 4 <= self.condition < 5:
            return "Pretty good condition"
        elif self.condition == 5:
            return "This is new, right?!"
class Item:
    def __init__(self, category=None, condition=0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition
        
    def __str__(self):
        return ("Hello World!")
        

    def condition_description(self):
        if self.condition == 0:
            return "One man's trash is another man's treasure."
        elif self.condition == 1:
            return "Very used and very discounted."
        elif self.condition == 2:
            return "Slightly ok condtion, slightly ok price."
        elif self.condition == 3:
            return "Ok condtion, ok price."
        elif self.condition == 4:
            return "Almost new!"
        elif self.condition == 5: 
            return "Like new, need the money."
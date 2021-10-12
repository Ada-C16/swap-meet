class Item:
    def __init__(self, category = ""): 
        self.category = category 
    def __str__(self):
        return "Hello World!"
    def condition_description(self): 
        if self.condition < 1: 
            return "poor"
        elif self.condition < 2: 
            return "bad" 
        elif self.condition < 3: 
            return "okay"
        elif self.condition < 4: 
            return "decent"
        elif self.condition < 5: 
            return "nearly new"
        else:
            return "this is so bad it does not have a condition description"

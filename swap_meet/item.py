class Item:

    def __init__(self, category=None, condition = 0):
        self.category = category if category is not None else ""
        self.condition = condition

    def __str__(self): 
        return f'Hello World!'
    
    def condition_description(self): 
        if self.condition == 0: 
            return("trash") 
        if self.condition == 1: 
            return("almost trash")
        if self.condition == 2:
            return ("meh")
        if self.condition == 3:
            return("better")
        if self.condition == 4:
            return("good")
        if self.condition == 5:
            return("best")

        

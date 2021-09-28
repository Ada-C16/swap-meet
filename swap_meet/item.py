class Item:
    
    def __init__(self, condition = None, category = None):
        if not category:
            category = ""
        self.category = category
        if not condition:
            condition = 0
        self.condition = round(condition, 1)
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Dumpster"
        elif self.condition == 1:
            return "Quite Worn"
        elif self.condition == 2:
            return "Gently Used" 
        elif self.condition == 3:
            return "Normal Use" 
        elif self.condition == 4:
            return "Slightly Worn" 
        else:
            return "New" 
            

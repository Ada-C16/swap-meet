



class Item:
    
    def __init__(self, condition = 0, category = ""):
        if category:
            self.category = category
        else:
            self.category = ''
        if condition :
            self.condition = condition
        else:
            self.inventory = 0
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition in range(0,3):
            return "Just get another, this one has reached the end of the line"
        if self.condition in range(3,5):
            return "A little beat up, but not too shabby"
        if self.condition in range(4,6):
            return "This is in good condition!Just get another, this one has reached the end of the line"



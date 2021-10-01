
class Item:
    #category is an empty string 
    def __init__(self, category = None, condition = 0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition  
        
    def __str__(self):
        return ("Hello World!")
    
    ### WAVE 5 ###

    def condition_description(self):
        if self.condition == 0:
            return "mint"
        elif self.condition == 1:
            return "new"
        elif self.condition == 2: 
            return "like new"
        elif self.condition == 3:
            return "used"
        elif self.condition == 4: 
            return "heavily used"
        elif self.condition == 5:
            return "don't use" 
        
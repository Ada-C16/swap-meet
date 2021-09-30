from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category = ""):
        self.category = category

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 1:
            return "Ew."
        elif self.condition == 2:
            return "Um."
        elif self.condition == 3:
            return "I mean, I guess."
        elif self.condition == 4:
            return "Acceptable."
        elif self.condition == 5:
            return "Yes."
        
        #return self.condition_description





  



    


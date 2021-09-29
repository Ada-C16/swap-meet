class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category 
        self.condition = condition
        
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        five_condition_desc = "go get it"
        four_condition_desc = "only if you get rid of something else"
        three_condition_desc = "only if you get rid of two other things"
        two_condition_desc = "fuggedaboutit, yoove down sized"
        one_condition_desc = "waste of time, move on"
        zero_condition_desc = "ah hell no"
        
        if self.category:
            if self.condition == 0.0:
                return zero_condition_desc
            
            if self.condition <= 1.0:
                return one_condition_desc
                
            elif self.condition <= 2.0:
                return two_condition_desc
                
            if self.condition <= 3.0:
                return three_condition_desc
                
            if self.condition <= 4.0:
                return four_condition_desc
                
            if self.condition <= 5.0:
                return five_condition_desc

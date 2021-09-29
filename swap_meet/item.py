class Item:
    
    def __init__(self,condition = 0,category = "" ):
        
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!" 
    
    def condition_description(self):
        if self.condition <= 2:
            return "Fair" 
        elif self.condition <= 5:
            return "Good Condition"
        else:
            return "Excellent condition" 
        
           
            
    

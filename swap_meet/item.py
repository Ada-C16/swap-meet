class Item:
#This is value only class because there are no methods..technically we have the constructor. 
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
        
        
        # if condition is None:
        #     self.condition = 0.0
        # else:
        #     self.condition = condition
        # if category is None:
        #     self.category= ""
        # else:
        #     self.category=category
    
 
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
            if self.condition <= 1:
                return("super used don't buy it")
            elif self.condition <= 2:
                return("pretty worn")
            elif self.condition  <=3:
                return("it's good for a date")
            elif self.condition <=4:
                return("Absolutely worth it")
            elif self.condition <=5:
                return("You bought it! YAY")

class Item:
    
    def __init__(self, category = "",condition = 0):
        #self.category = ""
        self.category = category 
        self.condition = condition

    def __str__(self):
        return("Hello World!")

    def condition_description(self, condition = 0):
        if self.condition == 0.0:
            return("Yikes on bikes")
        elif self.condition == 1.0:
            return("If things could talk...")
        elif self.condition == 2.0:
            return("Could be worse")
        elif self.condition == 3.0:
            return("Not too shabby")
        elif self.condition == 4.0:
            return("Practically new")
        elif self.condition == 5.0:
            return("Mint condition")
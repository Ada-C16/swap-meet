class Item:
    
    def __init__(self, condition = None, category = None):
        """
        Inizializes category and condition attributes
        """
        self.category = "" if not category else category
        self.condition = 0 if not condition else round(condition, 1)
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        """
        Returns condition description
        """
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
            

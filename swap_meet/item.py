class Item:
    def __init__(self, category="", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Really Shitty"
        elif self.condition == 1:
            return "A Little Less Shitty"
        elif self.condition == 2:
            return "Almost Average"
        elif self.condition == 3:
            return "Above the Mendoza Line"
        elif self.condition == 4:
            return "Slightly Less Excellent"
        elif self.condition == 5:
            return "Excellent"
        else:
            raise Exception(f"Condition must be an integer between 0 and 5. (Found {self.condition}).")

        

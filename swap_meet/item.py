class Item:
    def __init__(self, category = "", condition = 0): 
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        """
        Returning condition description based on item condition rating. 
        """
        if self.condition == 0:
            return "Are you sure this is an object?"
        
        if self.condition == 1: 
            return "Do you even love your friends? Throw this away."
        
        if self.condition == 2: 
            return "You can do better."

        if self.condition == 3: 
            return "An average conditioned object."
        
        if self.condition == 4: 
            return "Look at this fine object!"

        if self.condition == 5: 
            return "Wow! What a fancy, shiny, prestine object!"


class Item:
    def __init__(self, name="", condition=0, category = ""):
        self.name = name
        self.category = category
        self.condition = condition
        

## WAVE 3 ##
    def __str__(self):
        return "Hello World!" 


## Wave 5 ##
    def condition_description(self):
        condition_descriptions = {0: "That's a no for me, dawg", 1: "Poor", 2: "ehhh. it's ok", 3: "Good", 4: "Great!", 5: "You know this is mint condition!"}

        return condition_descriptions[self.condition]







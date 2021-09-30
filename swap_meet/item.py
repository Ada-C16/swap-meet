class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self, statement="Hello World!"):
        return statement
    
    def condition_description(self):
        if self.condition == 0 or self.condition <= 2.9:
            return 'Don\'t. Just don\'t.'
        elif self.condition == 3 or self.condition <= 3.9:
            return 'Likely involves repairs/stain removal. You\'ve been warned.'
        elif self.condition == 4 or self.condition <=5:
            return 'Is your friend sure they want to give this away? What a steal!' 



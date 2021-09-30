class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
        
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if 0 < self.condition < 1:
            return "Definitely gonna be used for parts"
        elif 1 <= self.condition < 2: 
            return "Probably gonna be used for parts"
        elif 2 <= self.condition < 3:
            return "Could be worse..."
        elif 3 <= self.condition < 4:
            return "Used but still functional and lookin' alright!"
        else:
            return "Lightly loved and works great!"
            

    

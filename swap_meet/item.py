class Item:
    def __init__(self, category = "", condition = 0.0,):
        self.category = category
        self.condition = condition

    def condition_description(self, condition):
        if self.condition <= 1:
            return "statement"
        if 1 < self.condition <= 2: 
            return "statement"
        if 2 < self.condition <= 3:
            return "statement"
        if 3 < self.condition <= 4:
            return "statement"
        if 4 < self.condition <= 5:   
            return "statement 5"
            
    def __str__(self):
        return "Hello World!"
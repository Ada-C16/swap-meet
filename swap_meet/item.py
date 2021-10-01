class Item:
    def __init__(self, category=None, condition=None):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0


    def __str__(self):
        return "Hello World!"


    def condition_description(self):
        if self.condition == 0:
            return "trash"
        
        if self.condition == 1:
            return "a memory of what it once was"

        if self.condition == 2:
            return "my ex left this"

        if self.condition == 3:
            return "good condition, but so last season"

        if self.condition == 4:
            return "the best you can do"

        if self.condition == 5:
            return "Beyonce owned this"
            

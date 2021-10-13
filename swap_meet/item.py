class Item:
    def __init__(self, category = "", condition = 0.0,):
        self.category = category
        self.condition = condition

    # Doing this made all the tests fail due to missing arguments, but
    # To add the age attribute, I think that I would:
    # def __init__(self, age, category = "", condition = 0.0,):
        # self.age = age
        # self.category = category
        # self.condition = condition

    # and then for each item category, I would change to:
    # def __init__(self, age, category="Electronics", condition=0.0):
    #     super().__init__(age, category, condition)
    
    def condition_description(self):
        if self.condition <= 1:
            return "Terrible"
        if 1 < self.condition <= 2: 
            return "Fair"
        if 2 < self.condition <= 3:
            return "Okay"
        if 3 < self.condition <= 4:
            return "Good"
        if 4 < self.condition <= 5:   
            return "Like New"
            
    def __str__(self):
        return "Hello World!"
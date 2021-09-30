class Item:
    def __init__(self, category= "", condition = 0, age = None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition >= 5:
            return "Brand spanking new!"
        elif self.condition >= 4:
            return "Brand new"
        elif self.condition >=3:
            return "Looks nice!"
        elif self.condition >= 2:
            return "Good"
        elif self.condition >= 1:
            return "Acceptable"
        else:
            return "Clearance item - no returns accepted.  Buy at your own risk!"
    
    def get_age(self):
        if self.age >= 20:
            return "Vintage"
        elif self.age >= 10:
            return "Retro"
        elif self.age >= 5:
            return "Contemporary"
        elif self.age >=1:
            return "Trending now"
        else:
            return "Brand new!"


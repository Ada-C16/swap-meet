class Item:
    def __init__(self, category = "", condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition >= 5:
            return "New Without Tags"
        elif self.condition >= 4:
            return "Mint Condition"
        elif self.condition >= 3:
            return "Gently Used"
        elif self.condition >= 2:
            return "Good Condition"
        elif self.condition >= 1:
            return "Some Visible Wear"
        else:
            return "Heavily Used"

    def get_age(self):
        if self.age >= 20:
            return "Vintage"
        elif self.age >= 10:
            return "Retro"
        elif self.age >= 5:
            return "Modern"
        elif self.age >= 1:
            return "Contemporary"
        else:
            return "Brand New"

    





    
    


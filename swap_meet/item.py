class Item:
    # Each Item will have an attribute named 'category'
    # Category is an empty string by default
    # After initialization, we can pass the keyword argument 'category'
    pass
    def __init__(self, category = "", condition = 0, age = None):
        self.category = category
        self.condition = condition
        self.age = age

    # stringify (convert to string) and instance of Item 
    # using str(), it returns "Hello World!"
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        # return string
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

    





    
    


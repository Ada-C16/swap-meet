class Item:
    def __init__(self,category = None, condition = 0, age = 0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return ("Hello World!")

    def condition_description(self):
        if self.condition ==0:
            return ("No rating")
        elif self.condition ==1:
            return("Very heavily used")
        elif self.condition ==2:
            return("Heavily used")
        elif self.condition ==3:
            return("Used")
        elif self.condition ==4:
            return("In good condition")
        elif self.condition ==5:
            return("Like new")
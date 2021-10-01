class Item:
    #Item is a parent class. Inheritance!
    def __init__(self, category = "", condition = 0):
            self.category = category
            self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition > 0 and self.condition < 1:
            return "This is garbage"
        elif self.condition == 1:
            return "Eh, you could do better"
        elif self.condition ==2:
            return "Not as bad as 1 but you can still do better"
        elif self.condition == 3:
            return "Not the best but not the worst"
        elif self.condition == 4:
            return "Much better, almost the best"
        elif self.condition == 5:
            return "This is the best you can get"
        else:
            return "What are you doing? Rating is not valid"

    
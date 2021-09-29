class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    def __str__(self):
        return "Hello World!"
    def condition_description(self):
        result = ""
        if self.condition == 5:
            result = "new"
        elif self.condition == 4:
            result = "open box"
        elif self.condition == 3:
            result = "used"
        elif self.condition == 2:
            result =="you don't want it"
        elif self.condition == 1:
            result == "trash"
        elif self.condition == 0:
            result == "OMG"
        return result

    


    

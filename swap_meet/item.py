

class Item:
    pass
    def __init__(self, category = '', condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(cls):
        return "Hello World!"
        
    def condition_description(self):
        if self.condition == 0:
            return "heavily used"
        if self.condition == 1.0:
            return "used"
        if self.condition == 2.0:
            return "some use"
        if self.condition == 3.0:
            return "good condition"
        if self.condition == 4.0:
            return "excellent"
        if self.condition == 5.0:
            return "brand new"
  
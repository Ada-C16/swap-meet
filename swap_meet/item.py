

class Item:
    
    def __init__(self, category = None, condition = None, age = None):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0
        self.age = age if age is not None else 0
        # age is from range 0-5 because we a bougie swap meet and don't allow things older than 5 years
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
  
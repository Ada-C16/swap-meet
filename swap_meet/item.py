class Item:
    def __init__(self, category= str(), condition =0, age =0):
        self.category = category
        self.condition = condition
        self.age = age        
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        value = self.condition
        if value >4:
            return 'Great condition'
        if value > 3:
            return "Used but in good conditon"
        if value < 3:
            return "Heavily used"
class Item:
    def __init__(self, category = None, condition = None):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <=2:
            return "This item is heavily used. I will give you a discount because it's in terrible shape"
        
        elif self.condition <=4:
            return "This item is in mint condition."
        
        else:
            return "This item is in awesome condition! No discounts!"
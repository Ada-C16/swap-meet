class Item:
    def __init__(self, category=None, condition = 0):
        self.category = category if category is not None else ""
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 2:
            return "This is heavily used."
        if self.condition is 3-4:
            return "This is in mint condition."
        if self.condition >4:
            return "This is in excellent condition."

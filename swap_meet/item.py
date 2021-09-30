class Item:
    
    def __init__(self, category = None, condition = 0.0):
        if category is None:
            self.category = ""
        else:
            self.category = category
        self.condition = condition

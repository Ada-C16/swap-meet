class Item:
    def __init__(self, category = None, condition = None):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0.0

    def __str__(self):
        return f'Hello World!'

    def condition_description(self):
        if 5 >= self.condition > 4:
            item_description = "New New"
        elif 4 >= self.condition > 3:
            item_description = "Almost New"
        elif 3 >= self.condition > 2:
            item_description = "Handmedown"
        elif 2 >= self.condition > 1:
            item_description = "Has Potential"
        elif 1 >= self.condition > 0:
            item_description = "It is,what it is"
        
        return item_description

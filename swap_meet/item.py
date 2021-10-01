class Item:
    def __init__(self, category=None, condition=None):
        self.category = "" if category is None else category
        self.condition = 0.0 if category is None else condition

    def __str__(self):
        return "Hello World!"
        
    def condition_description(self):
        if 5 >= self.condition > 4:
            item_description = "Mint"
        elif 4 >= self.condition > 3:
            item_description = "Near Mint"
        elif 3 >= self.condition > 2:
            item_description = "Very Fine"
        elif 2 >= self.condition > 1:
            item_description = "Good"
        elif 1 >= self.condition > 0:
            item_description = "Fair"

        return item_description

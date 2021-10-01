class Item:
    def __init__(self, category = None, condition = None):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        """This function provides a description of the condition of an item 
        depending on the value of the condition that ranges from 0-5."""
        if self.condition <=2:
            return "This item is heavily used. I will give you a discount \
                because it's in terrible shape!"
        
        elif self.condition <=4:
            return "This item is in mint condition. I will think about \
                giving you a discount..."
        
        else:
            return "This item is in perfect condition! Absolute no discounts!"
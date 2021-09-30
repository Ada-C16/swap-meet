class Item:
    """
    Class Item with method: condition_description
    """
    # class constructor
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    # stringify instances of class Item
    def __str__(self):
        return "Hello World!"

    # returns description of Item condition given condition(int) between 0 and 5
    def condition_description(self):
        try:
            if self.condition == 0.0:
                return "This has seen better days"
            elif self.condition == 1.0:
                return "Eh...maybe go with something else"
            elif self.condition == 2.0:
                return "Not terrible but not great"
            elif self.condition == 3.0:
                return "Average"
            elif self.condition == 4.0:
                return "Pretty good!"
            elif self.condition == 5.0:
                return "As good as it gets!"
            else:
                raise ValueError
        
        except ValueError:
            print("The condition must be a number between 0 and 5")



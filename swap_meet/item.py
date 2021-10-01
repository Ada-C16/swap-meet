class Item:
    """
    Item class has an attribute called category and condition with default values
    """

    # ********* Wave 1 **********

    def __init__(self, category="", condition=None):
        self.category = category
        self.condition = condition if condition is not None else 0

    # ********* Wave 2 **********

    def __str__(self):
        return "Hello World!"

    # ********* Wave 5 **********
    # this fuction discribes the condition and return a string
    # It is also a parent class for Clothing, Decor, Electronics Classes

    def condition_description(self):

        if self.condition == 5:
            return "Mint condition"
        elif self.condition == 4:
            return "Almost mint condition"
        elif self.condition == 3:
            return "Excellent condition"
        elif self.condition == 2:
            return "Good condition"
        elif self.condition == 1:
            return "Fair condition"
        elif self.condition == 0:
            return "Poor condition"

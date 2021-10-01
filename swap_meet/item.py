class Item:
    def __init__(self, category=None, condition=None):
        self.category = category if category is not None else ''
        self.condition = condition if condition is not None else 0

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "heavily used"
        if self.condition == 1:
            return "used"
        if self.condition == 2:
            return "some use"
        if self.condition == 3:
            return "good condition"
        if self.condition == 4:
            return "excellent"
        if self.condition == 5:
            return "brand new"

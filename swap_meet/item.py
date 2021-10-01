class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if 0 <= self.condition < 3:
            return "This is in poor condition"
        if 3 <= self.condition < 4:
            return "This is in good condition"
        if 4 <= self.condition < 5:
            return "This is in very good condition"
        if self.condition == 5:
            return "This is in excellent condition"

class Item:
    def __init__(self, category="", condition = float(0)):
        self.condition = condition
        self.category = category 

    def __str__(self):
        return f'Hello World!'

    def condition_description(self):
        if self.condition < 1:
            return "You shall not pass...inspection"
        elif self.condition < 2:
            return "This item may once have had value"
        elif self.condition < 3:
            return "This item's value has decreased from extensive wear"
        elif self.condition < 4:
            return "Fair condition should yield a fair price"
        elif self.condition < 5:
            return "Quality begets coin"
        elif self.condition == 5:
            return "In this condition, what's not to love.  Except maybe the price"
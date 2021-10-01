class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition > 0 and self.condition < 1:
            return "Burn it with fire"
        elif self.condition == 1:
            return "I wouldn't pick this up off the street"
        elif self.condition == 2:
            return "You sure?"
        elif self.condition == 3:
            return "stuck in the middle with you"
        elif self.condition == 4:
            return "close but no cigar (smoking is bad)"
        elif self.condition == 5:
            return "PERFECTION"
        else:
            return "Ayo invalid!"
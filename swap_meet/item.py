class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "It's giving 'Go home, Roger.' Don't do it. "
        elif self.condition == 1:
            return "Get this only if it's free."
        elif self.condition == 2:
            return "Ehh.. Buy it if it's the only one left and you absolutely need something like it."
        elif self.condition == 3:
            return "It could be better, but it could also be a lot worse."
        elif self.condition == 4:
            return "Oh so very lightly used. It's giving 'good enough.'"
        elif self.condition == 5:
            return "It's not gone get any better than this, honey!"
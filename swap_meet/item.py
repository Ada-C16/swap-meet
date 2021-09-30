class Item:
    
    def __init__(self, category = None, condition = 0.0):
        if category is None:
            self.category = ""
        else:
            self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <= 1 :
            return "POOR broken AND smells bad"
        elif self.condition <= 2:
            return "FAIR but smells bad..."
        elif self.condition <= 3:
            return "OK - doesn't stink!"
        elif self.condition <= 4:
            return "GOOD clean item"
        elif self.condition <= 5:
            return "EXCELLENT, smells of factory"
        else:
            return "fell off a truck... don't tell anyone where u got this"
        
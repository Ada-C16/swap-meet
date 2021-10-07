class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Not in good condition"
        elif self.condition <=1:
            return "Not in the best condition"
        elif self.condition <= 2:
            return "In okay condition"
        elif self.condition <= 3:
            return "In good condition"
        elif self.condition <= 4:
            return "In very good condition"
        else:
            return "Like new"
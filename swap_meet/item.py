class Item():
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "It's fallen apart"
        elif self.condition <= 1:
            return "Might fall apart tomorrow"
        elif self.condition <= 2:
            return "Barely acceptable"
        elif self.condition <= 3:
            return "That'll do"
        elif self.condition <= 4:
            return "Only used a few times"
        elif self.condition <= 5:
            return "Brand new. Never been used"
    


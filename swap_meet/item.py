class Item:
    def __init__(self, category ="", condition = 0):
        self.category = category
        self.condition = condition
        
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <= 5:
            return "minty fresh"
        if self.condition <= 4:
            return "light scracthes"
        if self.condition <= 3:
            return "lightly used"
        if self.condition <= 2:
            return "used"
        if self.condition <= 1:
            return "mwah"
        if self.condition <= 0:
            return "what are you doing? Put that down!"
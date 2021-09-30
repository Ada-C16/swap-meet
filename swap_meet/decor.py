class Decor:
    def __init__(self, category="Decor", condition=0.0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        if self.condition <= 1:
            return "Poor"
        if 1 < self.condition <= 2: 
            return "Fair"
        if 2 < self.condition <= 3:
            return "Neutral"
        if 3 < self.condition <= 4:
            return "Good"
        if 4 < self.condition <= 5:   
            return "Like New"

class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 0.0 or self.condition > 5.0:
            return "This is either really great or really gross. Proceed with caution."
        
        if self.condition == 1:
            return "Yikes on a bike. You don't want this."
        elif self.condition == 2:
            return "This is barely acceptable. Like if you scraped mold off of old bread."
        elif self.condition == 3:
            return "Well, you could do worse. You could also do much better."
        elif self.condition == 4:
            return "Wow! This is actually good! Grab it before someone else does!"
        elif self.condition == 5:
            return "This is basically new. I hope this didn't fall off a truck somewhere..."
        else:
            return "This is in between. Is it worth it?"
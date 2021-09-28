class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!" 

    def condition_description(self):
        description = "condition information unavailable"
        
        if self.condition == 0:
            description = "New with tags! Either a gift or they missed the return date."
        elif self.condition == 1:
            description = "New without tags. They changed their mind right away."
        elif self.condition == 2:
            description = "Excellent condition. They bought it, used it and then immediately found something better..."
        elif self.condition == 3:
            description = "Gently used. Previously loved, but little sign of wear."
        elif self.condition == 4:
            description = "Used. Some signs of wear. How much do you really want this and can you not find it elsewhere?"
        elif self.condition == 5:
            description = "Worn. Heavily used. Consider passing."

        return description
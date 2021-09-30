class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!" 

    def condition_description(self):
        description = "condition information unavailable"
        
        if self.condition >= 0 and self.condition < 1:
            description = "Worn. Heavily used. Consider passing."
        elif self.condition >= 1 and self.condition < 2:
            description = "Used. Has noticeable signs of wear. How much do you really want this and can you not find it elsewhere?"
        elif self.condition >= 2 and self.condition < 3:
            description = "Gently used. Previously loved, but little sign of wear."
        elif self.condition >= 3 and self.condition < 4:
            description = "Excellent condition."
        elif self.condition >= 4 and self.condition < 5:
            description = "New without tags. They changed their mind right away."
        elif self.condition == 5:
            description = "New with tags! Either a gift or they missed the return date."

        return description
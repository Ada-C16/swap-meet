class Item():

    def __init__(self, category = "", condition = None, age = None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition in range(0,1):
            return "Do what's best for all of us and don't spend your hard earned money on this! This is a scam."
        elif self.condition in range(1,2):
            return "You can probably get more bang for your buck at the swap meet down the road"
        elif self.condition in range(2,3):
            return "If you are a DIY magician you can very well turn this trash into a treasure"
        elif self.condition in range(3,4):
            return "This would be great gift for that person you aren't fond of but have an obligatory relationship with."
        elif self.condition == 5:
            return "I actually considered hidding this in the back to save it for myself. THIS IS IT"


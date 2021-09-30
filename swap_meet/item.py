class Item:

    # In order to make sure child class will pass in these two arguments, we should get rid of the default values. But to pass the test cases of this homework, we keep those default values. 
    def __init__(self, category = "", condition = 0, age = 0, price = 0):  # age is for optional enhancement
        self.category = category 
        self.condition = condition
        self.age  = age
        self.price = price

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if 1 > self.condition >= 0:
            return "Dump it now!"
        elif 2 > self.condition >=  1:
            return "Stinky and smelly. Put on mask and gloves."
        elif 3 > self.condition >= 2:
            return "Its owner welll utitlized it"
        elif 4 > self.condition >= 3:
            return "If you have room, you may consider take it."
        elif self.condition >= 4:
            return "Well preserved."
        else:
            return "New!"



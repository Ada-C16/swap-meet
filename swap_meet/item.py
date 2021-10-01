class Item:
    def __init__(self, category = "", condition = None, age = None):
        self.category = category
        self.condition = condition
        self.age = age
        
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition in range(0,1):
            return "This belongs in the landfill"
        elif self.condition in range(1,2):
            return "This is lowkey trash, too"
        elif self.condition in range(2,3):
            return "With a litte bit of love, this could work"
        elif self.condition in range(3,4):
            return "Worth keeping for yourself or a friend"
        elif self.condition in range(4,5):
            return "Could actually make for a decent gift"
        elif self.condition == 5:
            return "She's a keeper"
        else:
            return "Rating invalid. Check condition attribute value is between 0-5."
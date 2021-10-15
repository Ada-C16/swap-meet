

class Item:
    def __init__(self, category = "test", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        condition = self.condition

        if 0 >= condition < 1:
            return "You should really lower your expectations"
        elif 1 >= condition < 2:
            return "You may not get alot for this"
        elif 2 >= condition < 3:
            return "thats fair"
        elif 3 >= condition < 4:
            return "You should get some good options for this"
        elif condition == 5:
            return "perfect"
        else:
            return "please enter a valid condition"
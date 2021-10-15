

class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        condition = self.condition

        if 0 >= condition < 1:
            return "eww no, are we a joke to you?"
        elif 1 >= condition < 2:
            return "listen, Soo you agree this is trash?"
        elif 2 >= condition < 3:
            return "meh.. could be worse"
        elif 3 >= condition < 4:
            return "okay! now we are talking"
        elif condition == 5:
            return "perfect! thats what we are talking about"
        else:
            return "please enter a valid condition"
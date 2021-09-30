class Item:

    def __init__(self, category = "", condition = 0):

        self.category = category
        self.condition = float(condition)

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
            
        if 0 > self.condition < 1:
            return "recycle"

        elif 1 <=  self.condition < 2:
            return "I'll take that off your hands"

        elif 2 <= self.condition < 3:
            return "eh"

        elif 3 <= self.condition < 4:
            return "I could get the same thing cheaper eslewhere"

        else:
            return "I might be intereed"

      
        


    
    

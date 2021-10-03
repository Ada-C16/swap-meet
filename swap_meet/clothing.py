from swap_meet.item import Item
class Clothing(Item):


    def __init__(self, condition = 0 ):
        # super().__init__()
        # since super() just means "get my parent class"
        # this is equal to
        # Item.__init__()
        # which is defined in item.if self.condition == 3:py
        self.category= "Clothing" 
        self.condition = condition
        # if condition: 
        #     self.condition
      
    # automatically because of line 2
    # you have the condition_description method from item.py
    def __str__(self): 
        return "The finest clothing you could wear."

    
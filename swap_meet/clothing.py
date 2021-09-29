from swap_meet.item import Item

# do I need to use super() ?

class Clothing(Item):
    def __init__(self, category = "Clothing", condition = 0):
        self.condition = condition
        self.category = category

    def __str__(self):
        return "The finest clothing you could wear."
    
    
       

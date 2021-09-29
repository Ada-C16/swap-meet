from swap_meet.item import Item

# should I delete the duplicte attribute 'category' from Clothing, now that it is inheriting it from Item?\
# should category still be 'none' or an empty string now that I am defining it? 

class Clothing(Item):
    def __init__(self, category = "", condition = 0):
        super().__init__(category = "", condition = 0)
        self.condition = condition
        self.category = "Clothing"

    def __str__(self):
        return "The finest clothing you could wear."
    
    
       

from swap_meet.item import Item

class Clothing(Item):
   def __init__(self, condition = 0, category = ""):  # parameters to create item objects
       super().__init__(condition = condition, category = "Clothing")   #this is arguments when super is called
      
   def __str__(self):
       return "The finest clothing you could wear." 
    
   
   
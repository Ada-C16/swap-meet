from .item import Item

class Electronics(Item):
    def __init__(self, condition = 0, category = ""): #setting category = "Electronics here leaves a room for change when objects are created"
        super().__init__(condition, category = "Electronics") #whatever set here is the final value to be set to this objects attribute
    
    
    
    def __str__(self):
        return "A gadget full of buttons and secrets."

   
    
    
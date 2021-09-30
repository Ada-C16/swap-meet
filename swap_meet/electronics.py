from .item import Item

class Electronics(Item):
    def __init__(self,category = "", condition = 0): #setting category = "Electronics here leaves a room for change when objects are created"
        super().__init__(category = "Electronics",condition = condition) #whatever set here is the final value to be set to this objects attribute
       
    def __str__(self):
        return "A gadget full of buttons and secrets."
    
    
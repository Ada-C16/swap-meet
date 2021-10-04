from swap_meet.item import Item

class Electronics(Item):


    def __init__(self,condition = 0 ):
        self.category  = "Electronics" 
        self.condition = condition
        #super().__init__(condition=condition)
   
    def __str__(self): 
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        return super().condition_description(self)
        #pass
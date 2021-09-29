from swap_meet.item import Item


class Decor(Item):
   def __init__(self, condition = None, category = "Decor"):
       super().__init__(category, condition)
    #    self.category = "Decor"
    #    if not condition:
    #        self.condition = 0
    #    self.condition = condition  
   def __str__(self) -> str:
       return "Something to decorate your space."

   
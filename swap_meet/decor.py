from swap_meet.item import Item


from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category="Decor", condition=0):
        super().__init__(category, condition)
        
    def __str__(self, statement="Something to decorate your space."):
        return super().__str__(statement)
    
    def condition_description(self):
        return super().condition_description()

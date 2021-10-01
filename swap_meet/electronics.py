from swap_meet.item import Item

class Electronics(Item):
    def __init__ (self, condition = 0):
        super().__init__(condition = 0, category = "")
        self.category = 'Electronics'
        if condition :
            self.condition = condition
        else:
            self.inventory = 0
    

    def __str__(self):
        return "A gadget full of buttons and secrets."
        
    
    # def condition_description(self):
    #     electronics_description = super().condition_description()
    #     return electronics_description


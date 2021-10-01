from swap_meet.item import Item

class Electronics(Item):
    def __init__ (self, category ="",condition=0):
        super().__init__("Electronics", condition) #super pulls inhertiance from the base class which is item class
        
    def __str__(self):
        return "A gadget full of buttons and secrets."


    # def condition_description(self):
    #     if self.condition == 0:
    #         return "minty fresh"
    #     if self.condition == 1:
    #         return "light scracthes"
    #     if self.condition == 2:
    #         return "lightly used"
    #     if self.condition == 3:
    #         return "used"
    #     if self.condition == 4:
    #         return "mwah"
    #     if self.condition == 5:
    #         return " heavenly used"
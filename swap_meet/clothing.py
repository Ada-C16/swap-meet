from swap_meet.item import Item
class Clothing(Item):
    def __init__ (self,category ="", condition = 0):
        super().__init__("Clothing", condition)
        
    def __str__(self):
        return "The finest clothing you could wear."

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

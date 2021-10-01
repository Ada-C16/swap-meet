from swap_meet.item import Item

class Clothing(Item):

    def __init__ (self, condition = 0 ):
        super().__init__(condition = 0, category = "")
        self.category = 'Clothing'
        
        if condition :
            self.condition = condition
        else:
            self.inventory = 0

    def __str__(self):
        return "The finest clothing you could wear."

    # NOTE TO SELF
    # We don't need the condition description defined again(BELOW) 
    # since we are inheriting from the parent class it first 
    # search his clothing and then when it is not able to 
    # find it it automatically goes to the parents class

    # def condition_description(self):
    #     clothing_description = super().condition_description()
    #     return clothing_description
    

from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = 0):
        # self.category = category
        # self.condition = condition

        super().__init__(category = "Clothing", condition = condition) #do not use self #will get a weird error #assumes self is another argument 

        #super().condition_description()

        #super starts the lookup function the next level higher (in this case, Item)
        #we don't need line 10 because clothing isn't overriding the condition_description method
        #only need to use super if class has a method with the same name as the parent, and we need to call the 
        #method in the parent class 

    def __str__(self):
        return "The finest clothing you could wear."

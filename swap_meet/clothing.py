from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, condition=0):
        super().__init__(condition, category="Clothing" )
# In the block of code above^^ I am creating a class "Clothing", that is a subclass of a superclass "Item", I am passing the
#keyword argument "condition=0". Clothing inherits from Item its state and behavior. By calling
#the method super(). passing to this function the condition and category parameters, this last one set to "Clothing" 
#in order to make it inmutable when instantiating I am calling the methods in Item and adjusting it to this class.    

       
    def __str__(self):
        return "The finest clothing you could wear."

   



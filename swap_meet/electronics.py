from swap_meet.item import Item
class Electronics(Item):
    def __init__(self,condition=0):
        super().__init__(condition, category="Electronics")
# In the block of code above^^ I am creating a class "Electronics", that is a subclass of a superclass "Item", I am passing the
#keyword argument "condition=0". Decor inherits from Item all the state and behavior. By calling
#the method super(). passing to this function the condition and category parameters, this last one set to "Electronics" 
#in order to make it inmutable when instantiating I am calling the methods in Item and adjusting it to this class.
       
    def __str__(self):
        return "A gadget full of buttons and secrets."

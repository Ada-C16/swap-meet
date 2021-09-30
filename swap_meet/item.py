class Item:
    def __init__(self, condition=0, category=""):
        self.category=category
        self.condition=condition
# In the block of code above^^ I am creating a class "Item", I am passing the
#keyword argument "condition=0". Defining the attributes that will be instantiated.
        
    def __str__(self):
        return "Hello World!"
    
#With this method we are returning a description to the objects according to the value in the condition attribute 
    def condition_description(self):
        if self.condition>=0 and self.condition<=2.0:
            return "Still works"
        elif self.condition <=4.0:
            return "Plenty of life in it"
        elif self.condition<=5.0:
            return "Like new"
        
    
        
     
       
    

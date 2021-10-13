class Item:
   def __init__(self,condition = 0, category = ""):
      
       self.category = category
       self.condition = condition 
   
   def __str__(self):
       return "Hello World!"

   def condition_description(self):
       condition_list = ["Condition unknown", "heavily used item", "can be reused with modification",\
           "Good condition", "Excellent condition", "unbelievable" ]
       return condition_list[self.condition] 
            


    

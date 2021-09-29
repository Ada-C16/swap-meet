class Item:
   def __init__(self, category = "", condition = 0):
       if not category:
           category =  ""
       self.category = category
       self.condition = condition 
   
   def __str__(self):
       return "Hello World!"

   def condition_description(self):
        if self.condition == 0:
            return "Condition unknown"
        elif 0 < self.condition <= 1:
            return "heavily used item"
        elif 1 < self.condition <= 2:
            return "can be reused with modification"
        elif 2 < self.condition <= 3:
            return "can be resued with slight modification"
        elif 3 < self.condition <= 4:
            return "Good condition"
        elif 4 < self.condition <= 5:
            return "Excellent condition"


    

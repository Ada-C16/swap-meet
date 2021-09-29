class Item:
    def __init__(self, category = "", condition = 0):
      self.category = category 
      self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            print("needs some love")
        elif self.condition == 1:
            print("heavily loved")
        elif self.condition == 2:
            print("used condition")
        elif self.condition == 3:
            print("some signs of wear")
        elif self.condition == 4:
            print("almost new")
        elif self.condition == 5:
            print("mint")
        
    
     

    

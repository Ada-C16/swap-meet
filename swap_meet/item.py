class Item:
    #Wave 02
    def __init__(self,category= "", condition = 0):
        self.category = category 
        self.condition = condition
    
    #Wave 03
    def __str__(self):
        return "Hello World!"

    #Wave 05 
    def condition_description(self ):
        condition = self.condition
        if condition >= 0 and condition < 1:
            description = "yikes,raggedy, on its last leg"
        if condition >= 1 and condition < 2:
            description = "eek,heavy use,'rough around the edges'"
        if condition >= 2 and condition < 3:
            description = "eh,well used"
        if condition >= 3 and condition < 4:
            description = "ok,expected wear and tear"
        if condition >= 4 and condition < 5:
            description = "good,light use"
        if condition == 5:
            description = "superb,outstanding,like new"
        return description
        

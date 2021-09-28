class Item:
    
    def __init__(self, category="", condition=0): 
       self.category = category
       self.condition = condition
       
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        descs = {
            0 : "absolutely foul",
            1 : "it's not the best, but it'll do",
            2 : "this is semi-functional",
            3 : "im okay with this",
            4 : "this went well",
            5 : "i love it"
        }
        
        return descs[self.condition]
        

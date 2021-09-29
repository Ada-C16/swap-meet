from .item import Item


class Electronics(Item):
    def __init__(self, category = "Electronics", condition =0):
        super().__init__(category, condition)
        # self.category = category
        
        # if not condition:
        #     condition = 0
        # self.condition = condition 

    def __str__(self):
        return "A gadget full of buttons and secrets."
    
    
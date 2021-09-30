class Item:
    def __init__(self, category="", condition=0, id="Hello World!"):
        self.id = id
        self.category = category
        self.condition = condition

    def __str__(self):
        return str(self.id)
        
    def condition_description(self):
        if self.condition <= 1:
            return("deplorable, not worth the swap")
        elif self.condition <=3:
            return("ehhh, I mean if you must")
        elif self.condition == 4:
            return("they took pretty good care of this item")
        elif self.condition == 5:
            return("wow, this thang almost brand new!")

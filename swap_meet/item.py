class Item:
    def __init__(self, category=None, condition=0):
        self.category = category if category is not None else ""
        self.condition = condition 

    def __str__(self):
        return 'Hello World!'

    def condition_description(self):
        """
        Takes no parameters, returns a str
        that describes the item condition 
        based on a scale from 0 to 5 
        """
        if self.condition == 0:
            return "Has been loved A LOT."
        elif self.condition == 1:
            return "Has seen better days."
        elif self.condition == 2:
            return "Just some minor wear and tear."
        elif self.condition == 3:
            return "Just dandy."
        elif self.condition == 4:
            return "In good condition."
        elif self.condition == 5:
            return "In mint condition."
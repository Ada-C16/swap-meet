class Item:
    def __init__(self, category ='', condition = 0):
        self.category = category
        self.condition = condition
    def __str__(self):
        return 'Hello World!'

    def condition_description(self):
        if self.condition > 0 and self.condition <1.1:
            return 'Very Bad Condition'
        elif self.condition >= 1.1 and self.condition <2.1:
            return 'Pretty Bad Condition'
        elif self.condition >= 2.1 and self.condition <3.1:
            return 'Acceptable Condition'
        elif self.condition >= 3.1 and self.condition <4.1:
            return 'Pretty Good Condition'
        elif self.condition >= 4.1 and self.condition <5.1:
            return 'Very Good Condition'


    

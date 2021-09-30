class Item:
    def __init__(self, category = None, condition = None):
        if not category:
            category = ""
        self.category = category
        if not condition:
            condition = 0
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return 'mint'
        elif self.condition == 4:
            return 'excellent, used only 1 time'
        elif self.condition == 3:
            return 'good, used but works fine'
        elif self.condition == 2:
            return 'heavily used, needs some repairment'
        elif self.condition == 1:
            return 'not functioning, it can be your new project'
        else:
            return 'no description available'

    

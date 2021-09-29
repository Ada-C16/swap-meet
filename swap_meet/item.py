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
            print('mint')
        elif self.condition == 4:
            print('excellent, used only 1 time')
        elif self.condition == 3:
            print('good, used but works fine')
        elif self.condition == 2:
            print('heavily used, needs some repairment')
        elif self.condition == 1:
            print('not functioning, it can be your new project')
        else:
            print('no description available')

    

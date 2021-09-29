class Item:
    def __init__(self, category=None, condition=0):
        self.category = category if category is not None else ""
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self, condition=0):
        condition_num = int(condition)
        conditions = {
            0: "This should probably be in the free box.",
            1: "You could say that it is well-loved",
            2: "Hand me down round seven.",
            3: "There is potential here.",
            4: "Honestly, what a score.",
            5: "Still has the tags."
        }
        self.condition = conditions[condition]
        print(self.condition)

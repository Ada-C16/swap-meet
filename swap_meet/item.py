class Item:
    def __init__(self, category=None, condition=0):
        self.category = category if category is not None else ""
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        condition_num = int(self.condition)
        conditions = {
            0: "This should probably be in the free box.",
            1: "You could say that it is well-loved?",
            2: "Hand me down round seven.",
            3: "There is potential here.",
            4: "Honestly, what a score.",
            5: "Still has the tags."
        }
        item_condition = conditions[condition_num]
        return item_condition
        
        # if self.condition == 0:
        #     return "This should probably be in the free box."
        # if self.condition == 1:
        #     return "You could say that it is well-loved?"
        # if self.condition == 2:
        #     return "Hand me down round seven."
        # if self.condition == 3:
        #     return "There is potential here."
        # if self.condition == 4:
        #     return "Honestly, what a score."
        # if self.condition == 5:
        #     return "Still has the tags."

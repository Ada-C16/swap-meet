class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "It's on its last leg."
        if self.condition == 1:
            return "It could be worse, but just barely."
        if self.condition == 2:
            return "It's seen better days, but it'll get the job done."
        if self.condition == 3:
            return "Not too shabby if I do say so myself."
        if self.condition == 4:
            return "If you squint, it's brand new!"
        if self.condition == 5:
            return "Well I'll be! This is brand spanking new!" 


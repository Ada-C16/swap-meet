class Item:
    def __init__(self, name="", condition=0, age=None, category=""):
        self.name = name
        self.category = category
        self.condition = condition
        self.age = age

    def condition_description(self):
        if self.condition == 5:
            return "Top of the line, there's nothing like this out there"
        elif self.condition == 4:
            return "Pretty great but there may be a couple microscratches, bent corners, etc"
        elif self.condition == 3:
            return "Just your run of the mill item, nothing special here"
        elif self.condition == 2:
            return "I mean it *probably* works? Right?"
        elif self.condition == 1:
            return "This is being traded for parts"
        else:
            return "No one remembered to update the condition, so we have no idea!"

    def __str__(self):
        return "Hello World!"

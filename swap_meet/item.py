class Item:
    def __init__(self, condition = 0, category = ""):
        self.condition = condition
        self.category = category

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "One person's trash… might still just be trash."
        if self.condition == 1:
            return "My cat loved this."
        if self.condition == 2:
            return "Scour the internet for a manual and you'll probably figure it out?"
        if self.condition == 3:
            return "🤠"
        if self.condition == 4:
            return "Your cat will love this."
        if self.condition == 5:
            return "MINT 👌"
class Item:
    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.age = age
        if condition != 0:
            self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if 0 <= self.condition < 1:
            return "Trash"
        elif 1 <= self.condition < 2:
            return "Almost Trash"
        elif 2 <= self.condition < 3:
            return "Okay"
        elif 3 <= self.condition < 4:
            return "Good"
        elif 4 <= self.condition < 5:
            return "Pretty Good"
        else:
            return "Brand new. Good job!"
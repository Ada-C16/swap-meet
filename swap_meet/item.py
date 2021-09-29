class Item:
    
    def __init__(self, condition=0, age=0, category=""):

        self.category = category.title()
        self.condition = condition
        self.age = age

    def __str__(self):

        return "Hello World!"

    def condition_description(self):
        return str(self.condition)
    

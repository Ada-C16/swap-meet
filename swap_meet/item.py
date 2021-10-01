class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return ("Hello World!")
    
    def condition_description(self):
        condition_statements = ["Terrible","Bad","OK","Good","Excellent"]
        return condition_statements[self.condition-1]
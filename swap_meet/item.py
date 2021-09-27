class Item:
    def __init__(self, category = "", condition = 0.0):
        # if not category:
        #     category = ""
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        return str(self.condition)



class Item:
    def __init__(self, category= "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition >= 5:
            return "Brand Spanking New!"
        elif self.condition >= 4:
            return "Brand New"
        elif self.condition >=3:
            return "Looks good!"
        elif self.condition >= 2:
            return "Alright"
        elif self.condition >= 1:
            return "Acceptable"
        else:
            return "buy at your own risk"


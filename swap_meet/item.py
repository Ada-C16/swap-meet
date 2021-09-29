class Item():
    def __init__(self, category =str(""), condition= 0, age=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        description_rating= {0: "Fit for compost",
        1: "Piece of Junk",
        2: "Flawed and very used, but works",
        3: "Visibly used might have some imperfections",
        4: "Lightly used Item no imperfections",
        5: "New"
        }
        return description_rating[self.condition]

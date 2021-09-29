class Item:
    def __init__(self, category="", condition=None):
        self.category = category if category is not None else ""
        self.category = category

    def __str__(self):
        return 'Hello World!'

    def condition_description(self):
        if self.condition == 0:
            return "You'd be doin' me a favor."
        elif self.condition == 1:
            return "Just some minor wear and tear."
        elif self.condition == 2:
            return "Has seen better days."
        elif self.condition == 3:
            return "In ok condition."
        elif self.condition == 4:
            return "In good condition."
        elif self.condition == 5:
            return "In mint condition."
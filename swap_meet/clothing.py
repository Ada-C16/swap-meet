class Clothing:
    def __init__(self, category='', condition=0):
        self.category = "Clothing"
        self.condition = condition
    def __str__(self):
        return f"The finest clothing you could wear."
    def condition_description(self):
        if self.condition<=0:
            return f"bad condition"
        elif self.condition<=1:
            return f"Far below Average Condition."
        elif self.condition<=2:
            return f"Below Average Condition."
        elif self.condition<=3:
            return f"average."
        elif self.condition<=4:
            return f"Above average."
        elif self.condition<=5:
            return f"Good condition."


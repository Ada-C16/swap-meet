class Electronics:
    def __init__(self, category='', condition=0):
        self.category="Electronics"
        self.condition = condition
    def __str__(self):
        return f"A gadget full of buttons and secrets."
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

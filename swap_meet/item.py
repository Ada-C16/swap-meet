class Item:
    def __init__(self,condition=0.0, category=''):
        self.category=category
        self.condition=condition
    def __str__(self):
        return f"Hello World!"
    def condition_description(self):
        if self.condition==0.0:
            return f"Bad condition."
        elif self.condition==1.0:
            return f"Subpar"
        elif self.condition==2.0:
            return f"slightly below average."
        elif self.condition==3.0:
            return f"average."
        elif self.condition==4.0:
            return f"Above average."
        elif self.condition==5.0:
            return f"Good condition."

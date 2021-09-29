class Electronics:
    def __init__(self,category=''):
        self.category="Electronics"
        self.condition=0.0
    def __str__(self):
        return f"A gadget full of buttons and secrets."
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
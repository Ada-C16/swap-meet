class Electronics:
    def __init__(self, category="Electronics", condition=0, id="A gadget full of buttons and secrets."):
        self.category = category
        self.id = id
        self. condition = condition

    def __str__(self):
        return str(self.id)

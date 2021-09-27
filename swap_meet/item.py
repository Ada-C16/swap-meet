class Item:
    def __str__(self) -> str:
        return self.descrip
    def __init__(self, descrip=None, category=None, condition=None):
        self.descrip = descrip or "Hello World!"
        self.category = category or ""
        self.condition = condition or 0.0
    def condition_description(self):
        return "Condition " + str(self.condition)
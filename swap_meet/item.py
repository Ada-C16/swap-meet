class Item:
    def __str__(self) -> str:
        return self.descrip
    def __init__(self, descrip=None, category=None, condition=None):
        self.descrip = descrip or "Hello World!"
        self.category = category or ""
        self.condition = condition or 0.0
    def condition_description(self):
        conditions = {
            5: "This is definitely an item",
            4: "An object",
            3: "Pretty sure it's a thing",
            2: "Can't tell what's going on here",
            1: "Notions of form and substance",
            0: "What",
        }
        return conditions[int(self.condition)]
class Item:
    def __init__(self, category=None, condition=0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition

    def condition_description(self):
        descriptions = [
            "horrible",
            "really really bad",
            "really bad",
            "not okay",
            "okay",
            "fine",
        ]
        return descriptions[round(self.condition)]

    def __str__(self):
        return "Hello World!"

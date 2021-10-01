class Item:
    def __init__(self, category=None, condition=0.0):
        self.category=category if category is not None else ""
        self.condition=condition
    def __str__(self):
        return f'Hello World!'
    def condition_description(self, condition):
        descriptions={
            0:"Brand New",
            0.5: "Like New",
            1.0: "Lightly Used",
            1.5: "Used",
            2: "Normal Wear-and-Tear",
            2.5: "Rough Around the Edges",
            3: "Seen Better Days",
            3.5: "Lightly Usable",
            4: "Could Use for Parts",
            4.5: "Why Are You Selling This",
            5: "Hazardous Waste"
        }
        for rating in descriptions:
            if rating == condition:
                return descriptions[rating]
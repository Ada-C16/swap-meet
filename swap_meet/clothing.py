from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category="Clothing", age=-1, condition=0):
        super().__init__(category, age, condition)

    def __str__(self):
        return "The finest clothing you could wear."

from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition=0):
        super().__init__(category="Decor", condition=condition, id="Something to decorate your space.")

    def __str__(self):
        return str(self.id)

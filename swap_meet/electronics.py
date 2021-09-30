from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, category='Electronics', condition=0):
        super().__init__(category, condition)

    def __str__(self, statement='A gadget full of buttons and secrets.'):
        return super().__str__(statement)

    def condition_description(self):
        return super().condition_description()
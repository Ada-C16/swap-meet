from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = 0):
        super().__init__(category = "Clothing", condition = condition)

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        if self.condition == 1:
            return "Slightly used, but actually really used and probably should be thrown away"
        elif self.condition == 2:
            return "Used, somewhat used, slightly used, or not at all used but probably used"
        elif self.condition == 3:
            return "Moderately new, could mean used or not used or new and maybe it's not new?"
        elif self.condition == 4:
            return "New-ish, not necessarily new and not necessarily used"
        elif self.condition == 5:
            return "Unsure if used so will mark as new"
# wave 1
class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []

    def add(self, item):
        self.inventory.append(item)
        return item

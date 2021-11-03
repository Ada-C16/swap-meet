class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        updated_inventory = self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            updated_inventory = self.inventory.remove(item)
        else: 
            item = False
        return item
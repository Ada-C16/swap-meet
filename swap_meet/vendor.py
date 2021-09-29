class Vendor:
    def __init__(self, inventory = None ):
        self.inventory = inventory if inventory is not None else []

    def add(self, inventory_item):
        self.inventory.append(inventory_item)
        return inventory_item

    def remove(self, inventory_item):
        if inventory_item in self.inventory:
            self.inventory.remove(inventory_item)
            return inventory_item
        else:
            return False

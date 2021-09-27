class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, vendor_b, item_a, item_b):
        if item_a in self.inventory and item_b in vendor_b.inventory:
            self.inventory.remove(item_a)
            vendor_b.inventory.remove(item_b)

            self.inventory.append(item_b)
            vendor_b.inventory.append(item_a)

            return True
        return False

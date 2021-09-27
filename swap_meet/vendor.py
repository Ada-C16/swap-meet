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

    def swap_first_item(self, vendor_b):
        if len(self.inventory) and len(vendor_b.inventory):
            return self.swap_items(vendor_b, self.inventory[0], vendor_b.inventory[0])
        return False

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        return max(items, key=lambda x: x.condition) if items else None

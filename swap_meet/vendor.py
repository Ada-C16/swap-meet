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

    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory and their_item in other.inventory:
            self.inventory.remove(my_item)
            other.inventory.remove(their_item)

            self.inventory.append(their_item)
            other.inventory.append(my_item)

            return True
        return False

    def swap_first_item(self, vendor_b):
        if len(self.inventory) and len(vendor_b.inventory):
            return self.swap_items(vendor_b, self.inventory[0], vendor_b.inventory[0])
        return False

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        return max(items, key=lambda x: x.condition) if items else None

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_item, their_item)

from operator import attrgetter


class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        return items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.add(vendor.remove(their_item))
            vendor.add(self.remove(my_item))
            return True
        return False

    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory:
            my_first, their_first = self.inventory[0], vendor.inventory[0]
            return self.swap_items(vendor, my_first, their_first)
        return False

    def get_best_by_category(self, category):
        in_cat = [item for item in self.inventory if item.category == category]
        if in_cat:
            return max(in_cat, key=attrgetter("condition"), default=None)

    def swap_best_by_category(self, other, my_priority, their_priority):
        for_me = other.get_best_by_category(my_priority)
        for_them = self.get_best_by_category(their_priority)
        return self.swap_items(other, for_them, for_me)

from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.category ==  category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, vendor, my_item, their_item):
        try:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
        except ValueError:
            return False
        try:
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
        except ValueError:
            self.inventory.append(my_item)
            vendor.inventory.remove(my_item)
            return False
        return True

    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory:
            return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        else:
            return False
    
    def get_best_by_category(self, category):
        matches_category = self.get_by_category(category)
        best_item = None
        if matches_category:
            best_item = max(matches_category, key = lambda item : item.condition)
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if my_best_item and their_best_item:
            self.swap_items(other, my_best_item, their_best_item)
            return True
        else:
            False
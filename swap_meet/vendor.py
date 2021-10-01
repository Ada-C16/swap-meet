class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory


    def add(self, item):
        self.inventory.append(item)
        return item


    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False


    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items


    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.inventory.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True


    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        other_vendor.inventory.append(self.inventory[0])
        self.inventory.remove(self.inventory[0])
        self.inventory.append(other_vendor.inventory[0])
        other_vendor.inventory.remove(other_vendor.inventory[0])
        return True


    def get_best_by_category(self, category):
        best_find = None
        best_condition = 0.0
        for item in self.inventory:
            if item.category == category and item.condition > best_condition:
                best_condition = item.condition
                best_find = item
        return best_find


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_find = self.get_best_by_category(their_priority)
        other_best_find = other.get_best_by_category(my_priority)

        if my_best_find == None or other_best_find == None:
            return False

        self.swap_items(other, my_best_find, other_best_find)
        return True

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
        # try:
        #     self.inventory.remove(my_item)
        #     vendor.inventory.append(my_item)
        # except ValueError:
        #     return False
        # try:
        #     vendor.inventory.remove(their_item)
        #     self.inventory.append(their_item)
        # except ValueError:
        #     self.inventory.append(my_item)
        #     vendor.inventory.remove(my_item)
        #     return False
        # return True

        if my_item in self.inventory and their_item in vendor.inventory:
            self.add(their_item)
            self.remove(my_item)
            vendor.add(my_item)
            vendor.remove(their_item)
            return True
        else:
            return False

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
            return False

    def get_by_newest(self):
        """
        returns the newest item in inventory; if multiple newest items, returns the first one listed in the inventory
        """
        only_ages = []
        for item in self.inventory:
            if item.age != None:
                only_ages.append(item)
        if only_ages:
            newest_item = min(only_ages, key = lambda item : item.age)
            return newest_item
        else:
            return None

    def swap_by_newest(self, other):
        """
        
        """
        my_newest = self.get_by_newest()
        their_newest = other.get_by_newest()

        if my_newest and their_newest:
            self.swap_items(other, my_newest, their_newest)
            return True
        else: 
            return False
        
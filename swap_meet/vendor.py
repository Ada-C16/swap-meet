class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, adder):
        """Adds single item to inventory"""
        self.inventory.append(adder)
        return adder

    def remove(self,remove_it):
        """Removes single item from inventory"""
        if remove_it not in self.inventory:
            return False
        self.inventory.remove(remove_it)
        return remove_it

    def get_by_category(self, category_name):
        """Gets item object matching category name"""
        return [item for item in self.inventory 
        if item.category == category_name]

    def swap_items(self, vendor, my_item, their_item):
        """Swaps items in invenotry if present"""
        if (my_item not in self.inventory or
            their_item not in vendor.inventory):
            return False
        self.add(their_item), self.remove(my_item)
        vendor.add(my_item), vendor.remove(their_item)
        return True

    def swap_first_item(self, vendor):
        """Swaps first items in inventory"""
        if not self.inventory or not vendor.inventory:
            return False 
        self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        return True

    def get_best_by_category(self, type):
        """Gets highest raited condition item see item.py"""
        get_type = self.get_by_category(type)
        if not get_type:
            return None
        return max(get_type, key=lambda item: item.condition) 

    def swap_best_by_category(self, other, my_priority, their_priority):
        """Swaps items that has the best conditions"""
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best and their_best != None:
            self.swap_items(other, my_best, their_best)
            return True
        return False

    #added to swap by newest items assuming age ranges 0-4, 0 being the newest
    def get_newest_by_category(self, type):
        """Gets newest items by type"""
        get_type = self.get_by_category(type)
        if not get_type:
            return None
        return min(get_type, key=lambda item: item.age)

    def swap_by_newest(self, vendor, my_priority, their_priority):
        """Swaps newest items"""
        my_newest = self.get_newest_by_category(their_priority)
        their_newest = vendor.get_newest_by_category(my_priority)
        if my_newest and their_newest != None:
            self.swap_items(vendor, my_newest, their_newest)
            return True
        return False



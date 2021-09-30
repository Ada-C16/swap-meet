class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        for i in range(len(self.inventory)):
            if self.inventory[i] == item:
                return self.inventory.pop(i)
        return False

    def get_by_category(self, category):
        return [item for item  in self.inventory if item.category == category]
    
    def swap_items(self, Vendor, my_item, their_item):
        if my_item in self.inventory and their_item in Vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            Vendor.remove(their_item)
            Vendor.add(my_item)
            return True
        else: 
            return False

    def swap_first_item(self, Vendor):
        if len(self.inventory) > 0 and len(Vendor.inventory) > 0:
            self.swap_items(Vendor, self.inventory[0], Vendor.inventory[0])
            return True
        else: 
            return False

    def get_best_by_category(self, category):
        category_list = [item for item in self.inventory if item.category == category]
        if len(category_list) > 0:
            return max(category_list, key=lambda x: x.condition)
        else: 
            return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best and their_best:
            self.swap_items(other, my_best, their_best)
            return True
        return False


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

    def get_by_category (self, category):
        list_of_items = []
        for item in self.inventory:
            if item.category == category:
                list_of_items.append(item)
        return list_of_items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            vendor.add(my_item)
            vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if vendor.inventory and self.inventory:
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self,category):
        
        highest_condition = -1
        for item in self.inventory:
            if item.category == category:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    highest_condition_item = item
        if highest_condition == -1:
            return None
        else:
            return highest_condition_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        
        if my_best_item == None or their_best_item == None:
            return False
        else:

            self.swap_items(other, my_best_item, their_best_item)
                
            return True
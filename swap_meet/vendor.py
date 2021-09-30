from swap_meet.item import Item

class Vendor:

# Wave 1
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
        self.item = Item()

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else: 
            self.inventory.remove(item)
            return item

# Wave 2
    def get_by_category(self, category):
        inventory_items = []
        for item in self.inventory:
            if item.category == category:
                inventory_items.append(item)
        return inventory_items

# Wave 3
    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and my_item not in vendor.inventory and their_item in vendor.inventory and their_item not in self.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

# Wave 4
    def swap_first_item(self, vendor):
        if len(self.inventory) == False or len(vendor.inventory) == False:
            return False
        else: 
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
            return True

# Wave 6
    def get_best_by_category(self, category = ""):

        # categories = self.get_by_category(category)
        if len(self.get_by_category(category)) == False:
            return None
        
        best_by_category = max(self.get_by_category(category), key = lambda item : item.condition)

        

        return best_by_category

        # max_condition = 0

        # items_by_category = self.get_by_category(category)

        # for item in self.inventory:
        # for item in items_by_category:
        #     if item.condition >= max_condition:
        #         max_condition = item.condition
        #         return max_condition
        #         # else:
        #         #     max_condition = max_condition
        #         #     return max_condition
            # else:
            #     return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        if len(self.inventory) == False or len(other.inventory) == False:
            return False
        else: 
            return self.swap_items(other, self.get_best_by_category(category = their_priority), other.get_best_by_category(category = my_priority))

class Vendor():
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category_string):
        list_by_category =[]
        for item in self.inventory:
            if item.category == category_string:
                list_by_category.append(item)
        return list_by_category

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if len(self.inventory)> 1 and len(vendor.inventory)> 1:
        # storing first item of self.inventory and vendor. inventory in 2 variables
            my_first_item = self.inventory[0]
            their_first_item = vendor.inventory[0]
        # removing and adding items using variables
            self.inventory.remove(my_first_item)
            self.inventory.append(their_first_item)
            vendor.inventory.remove(their_first_item)
            vendor.inventory.append(my_first_item)
            return True
        else:
            return False
    def get_best_by_category(self, category):
    # using get_by_category method, storing result in new variable, items_by_category
    # items_by_category is now a list of objects that meet the category criteria
        items_by_category = self.get_by_category(category)
        if len(items_by_category)== 0:
            return None
        else:
            max_condition =max(item.condition for item in items_by_category)
            for item in items_by_category:
                if item.condition == max_condition:
                    return item

    def swap_best_by_category(self, other, my_priority, their_priority):
        
        my_best = self.get_best_by_category(their_priority)
        their_best =other.get_best_by_category(my_priority)
        if my_best == None or their_best == None:
            return False
        else:
            self.swap_items(other, my_best, their_best)
            return True








class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return item

    def get_by_category(self,category):
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self,vendor,my_item,their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        self.swap_items(vendor,self.inventory[0], vendor.inventory[0])
        return True


    def get_best_by_category(self,category):
        category_list = self.get_by_category(category)
        if not category_list:
            return None
        else:
            return max(category_list, key=lambda item:item.condition)


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if my_best_item == None:
            return False
        elif their_best_item == None:
            return False
        else:
            self.swap_items(other,my_best_item, their_best_item)
            return True

            
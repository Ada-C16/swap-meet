from .item import Item

class Vendor:

    def __init__(self, inventory = []):

        self.inventory = inventory


    def add(self, item):
        self.inventory.append(item)

        return item


    def remove(self, item):

        if item not in self.inventory:
            return False

        else:
            self.inventory.remove(item)
            return item


    def get_by_category (self, category):

        item_in_inventory_with_category = []

        for item in self.inventory:
            if item.category == category:
               item_in_inventory_with_category.append(item)

        return item_in_inventory_with_category


    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True

    def swap_first_item(self, friend):

        if not self.inventory or friend.inventory == []:
            return False
        
        else:
            
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True
            


    def get_best_by_category (self, category):


        best_item = None
        best_condition = 0

        for item in self.inventory:

            if item.category == category:
                if item.condition > best_condition:
            
                    best_condition = item.condition
                    best_item = item

        return best_item


    def swap_best_by_category (self, other, my_priority, their_priority):

        my_best =  self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        if not my_best or not their_best:

            return False

        self.swap_items(
            other,
            my_best,
            their_best)

        return True


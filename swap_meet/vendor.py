from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        # this allows us to add inventory items optionally   
        self.inventory = inventory

    def add (self, add_item):
        self.inventory.append(add_item) 
        return add_item
    
    def remove (self, remove_item):
        print(f"Removing {remove_item} from {self}")
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False

    def get_by_category (self, category):
        # check to see if category item is in inventory
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
            #if it is, append it to invetory list
                items_in_category.append(item)
        # return inventory list with items from that category
        return items_in_category

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)        
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        else:            
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True

    def get_best_by_category(self, best_category):
        # I already have a instance method that returns a list of items in category I am searching for.
        # Now I've stored category of items I am searching for in a new variable list
        list_best_items_category = self.get_by_category(best_category)
        # We can automatically have it return None now if it does not find category of item we are looking for 
        if not list_best_items_category:
            return None
        highest_condition_item = max(list_best_items_category, key=lambda item : item.condition)
        return highest_condition_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        # This return function will do job of return True or False and swap if there is a swap
        return self.swap_items(other, my_item, their_item)
        
        
        
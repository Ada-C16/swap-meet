from .item import Item

class Vendor:
    """Instantiates an object Vendor with an inventory.  Methods are adding or removing items from inventory,
    retrive items by specified category, swap items with another vendor, swap first in inventory item with first item 
    in inventory of another vendor, swap best item in specified category with the best item in specified category of 
    another vendor.
    """

    def __init__(self, inventory=None):
        """Instantiates an instance with an attribute inventory, by default an empty list"""
        self.inventory = inventory if inventory else []
    
    def add(self, new_item):
        """Adds new item to inventory list"""
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item):
        """Removes specified item from inventory list"""
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category):
        """Returns all items in ventory with a specified category"""
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, swapie_vendor, item_going_out, item_coming_in):
        """Swaps specified items between one instance of Vendor and another instance of Vendor"""
        if item_going_out in self.inventory and item_coming_in in swapie_vendor.inventory:
            swapie_vendor.add(item_going_out)
            self.remove(item_going_out)
            self.add(item_coming_in)
            swapie_vendor.remove(item_coming_in)
            return True
        else:
            return False
    
    def swap_first_item(self, swapie_vendor):
        """Swaps first items in inventory lists between one instance of Vendor and another instance of Vendor"""
        if len(self.inventory) != 0 and len(swapie_vendor.inventory) != 0:
            self.swap_items(swapie_vendor, self.inventory[0], swapie_vendor.inventory[0])
            return True
        else:
            return False
    
    def get_best_by_category(self, category):
        """Returns an item with best condition of a specified category"""
        items_of_category = self.get_by_category(category)
        best_condition = 0
        best_item = None
        for item in items_of_category:
            if item.condition >= best_condition:
                best_condition = item.condition
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        """Swaps specified items between one instance of Vendor and another instance of Vendor"""
        my_best_item_of_their_pref = self.get_best_by_category(their_priority)
        their_best_item_of_my_pref = other.get_best_by_category(my_priority)
        if my_best_item_of_their_pref == None or their_best_item_of_my_pref == None:
            return False
        elif len(self.inventory) != 0 and len(other.inventory) != 0:  
            self.swap_items(other, my_best_item_of_their_pref, their_best_item_of_my_pref)  
            return True
        else:
            return False
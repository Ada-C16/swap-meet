
from .item import Item



# WAVE 1
class Vendor:
    # constructor that is by default empty, but checks for input
    def __init__(self, inventory = [] ):
        if inventory :
            self.inventory = inventory
        else:
            self.inventory = []

    # method thats adds an item to inventory
    def add(self, item):
        self.inventory.append(item)
        return item

    # method that removes an item from inventory
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    # WAVE 2
    # method that adds items that are the same category to a list
    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list

    # WAVE 3
    # swaps items from one inventory to another
    def swap_items(self, another_vendor, my_item, their_item):
        if  my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            another_vendor.inventory.append(my_item)
            another_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True

    # WAVE 4
    def swap_first_item(self, another_vendor):
        if  self.inventory == [] or another_vendor.inventory == []:
            return False
        else:
            another_vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            self.inventory.append(another_vendor.inventory[0])
            another_vendor.inventory.remove(another_vendor.inventory[0])
            
            return True
    
    # WAVE 6
    def get_best_by_category(self, category):
        best_condition = 0.0
        best_item = ''

        for item in self.inventory:
            if item.category == category:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item
        
        if best_item:
            return best_item
        else:
            return None
    
    def swap_best_by_category(self, other, their_priority, my_priority):
        
        # my best item to give to them
        my_best_item = self.get_best_by_category(their_priority) 
        # their best item to give to me
        their_best_item = other.get_best_by_category(my_priority)

        if my_best_item and their_best_item:
            self.swap_items(other, my_best_item, their_best_item)
            return True
        else: 
            return False
            
        

    







        
        
    

        


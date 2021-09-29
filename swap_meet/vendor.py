from typing import ItemsView
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False 

    def get_by_category(self, category):
        items_by_category=[]

        for item in self.inventory:
            if item.category ==  category:
                items_by_category.append(item)
        return items_by_category
    

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.add(their_item) and self.remove(my_item)
        vendor.add(my_item) and vendor.remove(their_item)
        return True

    def swap_first_item(self,vendor):
        if bool(self.inventory)== False or bool(vendor.inventory)== False:
            return False
        return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
    
    def get_best_by_category(self,category):
        best_item = None
        best__condition = 0

        for item in  self.get_by_category(category):
            if item.condition > best__condition:
                best__condition = item.condition
                best_item= item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        if  my_item == None and their_item == None:
            return False
        else:
            return self.swap_items(other,my_item, their_item)
class Vendor:
    
    def __init__(self, inventory=[]): 
        self.inventory = inventory

    def add(self, new_item):
        """ Adds argument passed into new_item to Vendor's inventory list, and returns the new item. """
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item_to_remove):
        """ Removes argument passed into item_to_remove from Vendor's inventory list, and returns the removed item. """
        if item_to_remove not in self.inventory:
            return False
        self.inventory.remove(item_to_remove)
        removed_item = item_to_remove
        return removed_item
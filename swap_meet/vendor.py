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

    def get_by_category(self, category):
        """ Returns a list of items that have the category attribute given argument for category """
        inventory_items_in_category = []
        for item in self.inventory:
            if item.category == category:
                inventory_items_in_category.append(item)
        return inventory_items_in_category

    def swap_items(self, trading_vendor, my_item, their_item):
        """
        Takes in 3 arguments: another vendor instance, and item in the calling vendor's inventory, and an item from the
        the other vendor's inventory.
        
        If the items are in their expected inventories, the two given items are traded, and we return True. 
        
        Else, if either of the items aren't in their expected inventories, we return False.
        """
        if my_item not in self.inventory or their_item not in trading_vendor.inventory:
            return False
        for item in self.inventory:
            if my_item in self.inventory:
                trading_vendor.inventory.append(my_item)
                self.inventory.remove(my_item)
        for item in trading_vendor.inventory:
            if their_item in trading_vendor.inventory:
                self.inventory.append(their_item)
                trading_vendor.inventory.remove(their_item)
        return True
    
    def swap_first_item(self, trading_vendor):
        """ Takes in 1 argument: another vendor instance. Trades the first item in the calling instance's inventory
        with the first item in the other vendor's first item. Return True.
        """
        if not self.inventory or not trading_vendor.inventory:
            return False
        my_first = self.inventory[0]
        their_first = trading_vendor.inventory[0]
        # Swap my first item
        trading_vendor.inventory.append(my_first)
        self.inventory.remove(my_first)
        # Swap their first item
        self.inventory.append(their_first)
        trading_vendor.inventory.remove(their_first)

        return True


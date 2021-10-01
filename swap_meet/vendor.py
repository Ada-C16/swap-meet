class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
        
    def add(self,item):
        """This function takes an item and adds it to the inventory.
        It then returns the item"""
        self.inventory.append(item)
        return item

    def remove(self, item):
        """This function takes an item and removes the matching
        item from the inventory. After removing the item, this 
        function returns the removed item. If the item does not 
        exist in the inventory, the function returns False."""
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self, category):
        """This function takes in a category and returns a list of
        items in the inventory that matches the category passed."""
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, friend, my_item, their_item):
        """This function swaps an item in the Vendor's inventory
        with anotehr item in the friend's inventory. If the swap is 
        successful, the function returns True. Otherwise, returns
        False."""
        if my_item in self.inventory and their_item in friend.inventory:
            friend.inventory.append(my_item)
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            return True
        return False
    
    def swap_first_item(self, friend):
        """This function swaps the first item of this Vendor's inventory 
        with the first item of the friend's inventory. The function returns 
        True if the swap is successful. Otherwise, returns False."""
        if self.inventory and friend.inventory:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True
        return False

    def get_best_by_category(self, category):
        """This function returns the item with the best condition in
        the category passed in."""
        matched_categories = self.get_by_category(category)

        if not matched_categories:
            return None
        else:
            best_condition = 0
            best_item = None
            for matched_item in matched_categories:
                if matched_item.condition > best_condition:
                    best_condition = matched_item.condition
                    best_item = matched_item
            return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """This function swaps the best item of certain categories with
        another Vendor and returns True if the swap is successful. Otherwise,
        returns False."""
        my_best_item_matching_their_priority = self.get_best_by_category\
            (their_priority)
        their_best_item_matching_my_priority = other.get_best_by_category\
            (my_priority)

        if my_best_item_matching_their_priority == None \
            or their_best_item_matching_my_priority == None:
            return False
        else:
            self.swap_items(other, my_best_item_matching_their_priority,\
                their_best_item_matching_my_priority)
            return True

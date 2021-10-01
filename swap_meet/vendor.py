from swap_meet.item import Item #why here??

class Vendor:
    def __init__(self, inventory= None):
        if not inventory:    
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        """
        This method adds the item to our inventory.
        """
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        """
        This method will remove a matching item in our inventory.
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category): 
        """This method returns a list of Items in the inventory with that category"""
        items = []
        #self.category = category
        for item in self.inventory:             
            if item.category == category:  
                items.append(item)  
        return items

    def swap_items(self, friend, my_item, their_item):
        """It removes the my_item from this Vendor's inventory, and adds it to the friend's inventory
        It removes the their_item from the other Vendor's inventory, and adds it to this Vendor's inventory"""
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        self.remove(my_item)
        friend.add(my_item)  
        friend.remove(their_item)
        self.add(their_item)
        return True 

    def swap_first_item(self, friend):
        """Take in another vendor.
        Swap the first item in each vendor's inventory.
        Return True if the swap was completed successfully and False if not.
        These docstrings feel like they are just as long as the functions themselves, if not longer."""
        if not self.inventory or not friend.inventory:
            return False
        first_item = self.inventory[0]
        first_other_item = friend.inventory[0]

        self.inventory.append(first_other_item)
        friend.inventory.append(first_item)
        friend.inventory.remove(first_other_item)
        self.inventory.remove(first_item)
        return True

    def get_best_by_category(self, category): 
        """will get the item with the best condition in a certain category"""
        items = self.get_by_category(category)
        best_item = None
        for item in items:
            if best_item == None:
                best_item = item
            if item.condition > best_item.condition:
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        """will swap the best item of certain categories with another Vendor"""
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if not my_item and their_item:
            return False
        return self.swap_items(other, my_item, their_item)
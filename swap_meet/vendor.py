class Vendor:
    
    def __init__(self, inventory = None):
        """ 
        Initializes the inventory attribute
        """
        self.inventory = [] if not inventory else inventory # Turnery conditional expression

    def add(self, item):
        """
        Adds item to inventory
        """
        self.inventory.append(item)
        return item
        
    def remove(self, item):
        """
        Removes item from inventory
        """
        item_exists = False
        if item in self.inventory:
            self.inventory.remove(item)
            item_exists = True
        return item if item_exists else item_exists
    
    def get_by_category(self, category):
        """
        Returns list of items of a specified category
        """
        return [item for item in self.inventory if item.category == category]
    
    def swap_items(self, vendor, my_item, their_item):
        """
        Swaps my_item with their_item and updates respective vendors inventory
        """
        swap_good = False
        if (my_item in self.inventory) and (their_item in vendor.inventory):
            self.add(their_item)
            self.remove(my_item)
            vendor.add(my_item)
            vendor.remove(their_item)
            swap_good = True
        return swap_good

    def swap_first_item(self, vendor):
        """
        Swaps first item in inventory
        """
        swap_good = False
        if self.inventory and vendor.inventory:
            my_item = self.inventory[0]
            self.remove(my_item)
            vendor.add(my_item)
            their_item = vendor.inventory[0]
            self.add(their_item)
            vendor.remove(their_item)
            swap_good = True
        return swap_good
    
    def get_best_by_category(self, category):
        """
        Gets the best rated item of a specified category
        """
        items_in_category = [item for item in self.inventory if item.category == category]
        item_conditions =[item.condition for item in items_in_category]
        if not item_conditions:
            return None
        max_condition = max(item_conditions)
        best_by_category = [item for item in items_in_category if item.condition == max_condition]
        return best_by_category[0]
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Swaps best items of specified categorys for two vendors
        """
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        self.swap_items(other, my_item, their_item)
        return False if (my_item == None or their_item == None) else True


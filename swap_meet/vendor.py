class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_inventory(self):
        return self.inventory

    def get_by_category(self, category = ""):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)        
        return items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor_friend):
        if len(self.inventory) == 0 or len(vendor_friend.inventory) == 0:
            return False
        my_item = self.inventory[0]
        their_item = vendor_friend.inventory[0]
        self.swap_items(vendor_friend, my_item, their_item)
        return True
    
    def get_best_by_category(self, category):
        highest_rating = 0
        most_pristine_item = None
        
        for item in self.inventory:
            if item.category == category and item.condition >= highest_rating:
                highest_rating = item.condition
                most_pristine_item = item
        
        return most_pristine_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        
        if my_item == None or their_item == None:
            return False
        
        self.swap_items(other, my_item, their_item)
        return True
        
####################################################################################
    # def swap_items(self, vendor, my_item, their_item):
    #     if my_item in self.inventory and their_item in vendor.inventory:
    #         self.inventory.remove(my_item)
    #         vendor.inventory.append(my_item)
    #         vendor.inventory.remove(their_item)
    #         self.inventory.append(their_item)

    #         return True
    #     else:
    #         return False
    
    # def swap_first_item(self, vendor_friend):
    #     if len(self.inventory) == 0 or len(vendor_friend.inventory) == 0:
    #         return False
    #     else:
    #         my_item = self.inventory[0]
    #         their_item = vendor_friend.inventory[0]
    #         self.inventory[0] = their_item
    #         vendor_friend.inventory[0] = my_item
    #         return True
    
    # def get_best_by_category(self, category):
    #     highest_rating = 0
    #     most_pristine_item = None
    #     for item in self.inventory:
    #         if item.category == category and item.condition >= highest_rating:
    #             highest_rating = item.condition
    #             most_pristine_item = item

    #     return most_pristine_item
    
    # def swap_best_by_category(self, other, my_priority, their_priority):
    #     my_item = self.get_best_by_category(their_priority)
    #     their_item = other.get_best_by_category(my_priority)
        
    #     if my_item == None or their_item == None:
    #         return False
    #     else:
    #         self.inventory.remove(my_item)
    #         self.inventory.append(their_item)
    #         other.inventory.remove(their_item)
    #         other.inventory.append(my_item)

    #         return True
####################################################################################
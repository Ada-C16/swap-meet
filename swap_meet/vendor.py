class Vendor:
    
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        matching_items = []
        for item in self.inventory:
            if item.category == category:
                matching_items.append(item)
        return matching_items
    
    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.inventory.remove(my_item)
        vendor.inventory.append(my_item)
        vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True

    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False

        self_first_item = self.inventory[0]
        friend_first_item = vendor.inventory[0]

        return self.swap_items(vendor, self_first_item, friend_first_item)
        
        # self.inventory = self.inventory[1:]
        # vendor.inventory = vendor.inventory[1:]
        # self.inventory.append(friend_first_item)
        # vendor.inventory.append(self_first_item)
        # return True

    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        if len(category_items) == 0:
            return None

        best_item = None
        max_condition = 0

        for item in category_items:
            if item.condition > max_condition:
                best_item = item
                max_condition = item.condition
        return best_item
        
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if my_best_item == None or their_best_item == None:
            return False
        
        return self.swap_items(other, my_best_item, their_best_item)

        # self.inventory.remove(my_best_item)
        # other.inventory.remove(their_best_item)
        # self.inventory.append(their_best_item)
        # other.inventory.append(my_best_item)
        # return True
        




  

    
        


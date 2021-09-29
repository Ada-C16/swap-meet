class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category (self, category):
        list_of_items = []
        for item in self.inventory:
            if item.category == category:
                list_of_items.append(item)
        return list_of_items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            vendor.add(my_item)
            vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False

    #not working        
    def swap_first_item(self, vendor):
        if vendor.inventory and self.inventory:
            friends_first_item = vendor.inventory.remove(vendor.inventory[0])
            my_first_item = self.inventory.remove(self.inventory[0])
            vendor.inventory.append(my_first_item) 
            self.inventory.append(friends_first_item) 
            return True
        else:
            return False

    def get_best_by_category(self,category):
        
        highest_condition = -1
        for item in self.inventory:
            if item.category == category:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    highest_condition_item = item
        if highest_condition == -1:
            return None
        else:
            return highest_condition_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_condition = -1
        their_best_condition = -1
        
        my_best_item_matches_their_priority = None
        their_best_item_matches_my_priority = None

        for item in self.inventory:
            if item.category == their_priority:
                if item.condition > my_best_condition:
                    my_best_item_matches_their_priority = item
                    my_best_condition = item.condition
                
        if my_best_condition == -1:
            return False
        
        for item in other.inventory:
            if item.category == my_priority:
                if item.condition > their_best_condition:
                    their_best_item_matches_my_priority = item
                    their_best_condition = item.condition

        if their_best_condition == -1:
            return False
        
        self.swap_items(other, my_best_item_matches_their_priority, their_best_item_matches_my_priority)
            
        return True
class Vendor:
    def __init__ (self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item

    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else: 
            return False
        
    def get_by_category(self, category):
        category_inventory = []
        for item in self.inventory:
            if item.category == category:
                category_inventory.append(item)
        return category_inventory
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True

    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:           
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True 

    def get_best_by_category(self, category):
        highest_condition = 0
        highest_item = None 
        
        for item in self.inventory:
            if item.category == category:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    highest_item = item
        
        return highest_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best_item, their_best_item)


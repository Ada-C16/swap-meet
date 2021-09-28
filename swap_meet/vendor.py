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
    
    def get_by_category(self, category):
        category_count = [] 
        for item in self.inventory:
            if item.category == category:
                category_count.append(item)
        return category_count
    
    def swap_items(self, vendor, my_item, their_item):
        if (my_item in self.inventory) and (their_item in vendor.inventory):
            self.add(their_item)
            self.remove(my_item)
            vendor.add(my_item)
            vendor.remove(their_item)
            return True
        else:
            return False
    
    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory:
            my_item = self.inventory[0]
            self.remove(my_item)
            vendor.add(my_item)
            their_item = vendor.inventory[0]
            self.add(their_item)
            vendor.remove(their_item)
            return True
        else:
            return False
    
    def get_best_by_category(self, category):
        items_in_category = [item for item in self.inventory if item.category == category]
        item_conditions =[item.condition for item in items_in_category]
        if not item_conditions:
            return None
        else:
            max_condition = max(item_conditions)
        best_by_category = [item for item in items_in_category if item.condition == max_condition]
        return best_by_category[0]
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        self.swap_items(other, my_item, their_item)
        if my_item == None or their_item == None:
            return False
        return True


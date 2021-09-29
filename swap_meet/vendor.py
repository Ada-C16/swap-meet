
class Vendor:
    def __init__(self, inventory = None):
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
        
    def get_by_category(self, category = ""):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, Vendor, my_item, their_item):
        
        if my_item in self.inventory and their_item in Vendor.inventory:
        
            self.remove(my_item)
            Vendor.remove(their_item)
            self.add(their_item)
            Vendor.add(my_item)
            return True
        
        else:
            return False
        
    def swap_first_item(self, Vendor):
        if len(self.inventory) == 0 or len(Vendor.inventory) == 0:
            return False
    
        else:
            self.swap_items(Vendor, self.inventory[0], Vendor.inventory[0])
            return True
        
    def get_best_by_category(self, category):
        item_best = None
        
        for item in self.inventory:
          
            if item.category == category:
                if item_best is None:
                    item_best = item
                    
                else:
                    if item.condition > item_best.condition:
                        item_best = item
        return item_best
    
    def swap_best_by_category (self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        
        if my_item is None or their_item is None:
            return False
        
        else:
            self.swap_items(other, my_item, their_item)
            return True
        
        
class OtherVendor(Vendor):
    def __init__(self, inventory):
        super().__init__(inventory)
        self.inventory = inventory 
        
        

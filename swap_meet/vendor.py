
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
        
            self.remove([my_item])
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
            Vendor.inventory.remove(self.inventory[0])
            self.inventory.remove(Vendor.inventory[0])  
            return True
        
class OtherVendor(Vendor):
    def __init__(self, inventory = None):
        super().__init__(inventory)
        self.inventory = inventory
        
        

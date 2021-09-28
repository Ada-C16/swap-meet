
class Vendor:
    def __init__(self, inventory = []):
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
        
    def get_by_category(self, category = ""):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, Vendor, my_item, their_item):
        
        if len(self.inventory) == 0 or len(Vendor.inventory) == 0:
            return False
        
        else:
            self.inventory.remove(self.inventory[my_item])
            Vendor.inventory.remove(Vendor.inventory[their_item])
            self.inventory.add(Vendor.inventory[their_item])
            Vendor.inventory.add(self.inventory[my_item])
        return True
        
    def swap_first_item(self, Vendor):
        if len(self.inventory) == 0 or len(Vendor.inventory) == 0:
            return False
        else:
            Vendor.inventory.remove(self.inventory[0])
            self.inventory.remove(Vendor.inventory[0])  
            return True
        
class Other_Vendor(Vendor):
    def __init__(self, inventory = []):
        super().__init__(inventory)
        self.inventory = inventory
        
        

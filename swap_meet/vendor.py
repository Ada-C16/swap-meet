from .item import Item
class Vendor:
    def __init__(self, inventory=[]):
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
        return [item for item in self.inventory if item.category == Item(category=category).category]
    
    def swap_items(self, Vendor, my_item, their_item):
        
        if my_item in self.inventory and their_item in Vendor.inventory:
            Vendor.remove(their_item)
            self.add(their_item)
            Vendor.add(my_item)
            self.remove(my_item)
            return True
        else:
            print("over here")
            return False

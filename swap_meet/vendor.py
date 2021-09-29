from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
        self.item = Item()

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
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, vendor, my_item, their_item):
        if their_item in vendor.inventory and my_item in self.inventory:
            self.inventory.append(their_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            self.inventory.remove(my_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if len(self.inventory) != 0 and len(vendor.inventory) != 0:
            return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        else:
            return False


        
        




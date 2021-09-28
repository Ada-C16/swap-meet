from swap_meet.item import Item 

class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory
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

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.remove(their_item)
            self.inventory.append(their_item)
            return True 

    def swap_first_item(self, other_vendor):
        if len(self.inventory) != 0 and len(other_vendor.inventory) != 0: 
            other_vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            self.inventory.append(other_vendor.inventory[0])
            other_vendor.inventory.remove(other_vendor.inventory[0])
            return True
        else:
            return False
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else[]
        self.item = Item()

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, new_item):
        if new_item in self.inventory:
            self.inventory.remove(new_item)
            if new_item not in self.inventory:
                return new_item
        elif new_item not in self.inventory:
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

    def get_best_by_category(self, category =""):
        pass
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

    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category)
        if items_by_category == None:
            return None
            
        top_item_condition = 0
        top_item = None
        best_by_category = {}
        
        for item in items_by_category:
            best_by_category[item] = item.condition
        for item, item_condition in best_by_category.items():
            if item_condition > top_item_condition:
                top_item_condition = item_condition
                top_item = item
        return top_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        if len(self.get_by_category(their_priority)) == 0 or len(other.get_by_category(my_priority)) == 0:
            return False

        my_best_item = self.get_best_by_category(their_priority)
        vendor_best_item = other.get_best_by_category(my_priority)

        # if not my_best_item or not vendor_best_item:
        #     return False

        self.swap_items(other, my_best_item, vendor_best_item)
        return True

        




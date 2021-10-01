class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, inventory_item):
        self.inventory.append(inventory_item)
        return inventory_item

    def remove(self, inventory_item):
        if inventory_item in self.inventory:
            self.inventory.remove(inventory_item)
            return inventory_item
        else:
            return False

    # inventory is a list of item istances with each item having a category as an attribute
    # get_by_category filters inventory by category
    # items is a list of just the filtered item instances
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory:
            return False
        if their_item not in vendor.inventory:
            return False
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        self.add(their_item)
        return True
        
    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        vendor.add(self.inventory[0])
        self.remove(self.inventory[0])
        self.add(vendor.inventory[0])
        vendor.remove(vendor.inventory[0])
        return True

    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category)
        best_item = None
        highest_condition = 0
        for item in items_by_category:
            if item.condition > highest_condition:
                highest_condition = item.condition
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if their_best_item == None or my_best_item == None:
            return False
        self.swap_items(other, my_best_item, their_best_item)
        return True
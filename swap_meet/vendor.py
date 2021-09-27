class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        found_item = False
        for current_item in self.inventory:
            if current_item == item:
                self.inventory.remove(current_item)
                found_item = True
        if found_item:
            return item
        else:
            return False

    def get_by_category(self, select_category):
        items_by_category = []
        for item in self.inventory:
            if item.category == select_category:
                items_by_category.append(item)
        return items_by_category

    def swap_items(self, other_vendor, item_out, item_in):
        # are these two tests the most efficient route?
        if item_out in self.inventory and item_in in other_vendor.inventory:
            # remove my item from inv
            self.remove(item_out)
            # remove new item from other vendor's inv
            other_vendor.remove(item_in)
            # add new item to my inv
            self.add(item_in)
            # add item to other vendor's inv
            other_vendor.add(item_out)
            # return True
            return True
        # if items successfully added and removed, return True
        return False

    def swap_first_item(self, other_vendor): 
        if self.inventory and other_vendor.inventory:
            item_in = other_vendor.inventory[0]
            item_out = self.inventory[0]
            self.swap_items(other_vendor, item_out, item_in)
            return True
        return False
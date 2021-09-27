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

    def swap_items(self, vendor_name, item_out, item_in):
        # remove my item from inv
        self.remove(item_out)
        # add item to other vendor's inv
        vendor_name.add(item_out)
        # remove new item from other vendor's inv
        vendor_name.remove(item_in)
        # add new item to my inv
        self.add(item_in)
        return True



        
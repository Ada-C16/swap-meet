class Vendor:
    def __init__(self, inventory=None):
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

    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.category ==  category:
                items_in_category.append(item)
        return items_in_category
        
    def swap_items(self, vendor, my_item, their_item):
        try:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
        except ValueError:
            return False
        try:
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
        except ValueError:
            self.inventory.append(my_item)
            vendor.inventory.remove(my_item)
            return False
        return True
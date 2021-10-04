class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, selected_category):
        items_in_category = [item for item in self.inventory if item.category == selected_category]
        return items_in_category

    def swap_items(self, other_vendor, item_out, item_in):
        if not (item_out in self.inventory and item_in in other_vendor.inventory):
            return False
        self.remove(item_out)
        other_vendor.add(item_out)
        other_vendor.remove(item_in)
        self.add(item_in)
        return True

    def swap_first_item(self, other_vendor): 
        if not (self.inventory and other_vendor.inventory):
            return False
        item_in = other_vendor.inventory[0]
        item_out = self.inventory[0]
        self.swap_items(other_vendor, item_out, item_in)
        return True

    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        if not category_items:
            return None
        best_item = max(category_items, key= lambda i: i.condition)
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        if not (self.inventory and other.inventory):
            return False
        item_in = other.get_best_by_category(my_priority)
        item_out = self.get_best_by_category(their_priority)
        if item_in and item_out:
            return self.swap_items(other, item_out, item_in)
        return False
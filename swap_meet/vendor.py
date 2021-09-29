class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, friend_vendor, my_item, their_item):
            if (
                my_item not in self.inventory or
                their_item not in friend_vendor.inventory
                ):
                return False
            else:
                self.inventory.remove(my_item)
                friend_vendor.inventory.append(my_item)
                friend_vendor.inventory.remove(their_item)
                self.inventory.append(their_item)
                return True

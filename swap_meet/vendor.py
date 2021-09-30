class Vendor:

    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

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
        items_in_same_category = []

        for item in self.inventory:
            if item.category == category:
                items_in_same_category.append(item)

        return items_in_same_category

    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend_vendor.inventory:
            return False
        else:
            self.inventory.append(their_item)
            friend_vendor.inventory.remove(their_item)
            friend_vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            return True

    def swap_first_item(self, friend_vendor):
        if not self.inventory or not friend_vendor.inventory:
            return False
        else:
            self.swap_items(
                friend_vendor, self.inventory[0], friend_vendor.inventory[0])
            return True
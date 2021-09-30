class Vendor:
    def __init__(self, inventory = None):
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
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, vendor, my_item, their_item):
        if their_item not in vendor.inventory or my_item not in self.inventory:
            return False
        else:
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            return True

    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        else:
            friend_items = vendor.inventory
            friend_item = friend_items[1]
            my_items = self.inventory
            my_item = my_items[1]
            self.inventory.append(friend_item)
            vendor.inventory.append(my_item)
            vendor.inventory.pop([1])
            self.inventory.pop([1])
            return True

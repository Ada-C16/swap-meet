from .item import Item


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.category == category:
                result.append(item)
        return result

    def swap_items(self, vendor_friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor_friend.inventory:
            return False
        self.remove(my_item)
        vendor_friend.add(my_item)
        vendor_friend.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, vendor_friend):
        if self.inventory == [] or vendor_friend.inventory == []:
            return False
        vendor_friend.add(self.inventory[0])
        self.remove(self.inventory[0])
        self.add(vendor_friend.inventory[0])
        vendor_friend.remove(vendor_friend.inventory[0])
        return True

    def get_best_by_category(self, category):
        inventory_in_category = []
        for item in self.inventory:
            if item.category == category:
                inventory_in_category.append(item)
        if len(inventory_in_category) == 0:
            return None
        best_condition = inventory_in_category[0].condition
        winner = inventory_in_category[0]
        for item in inventory_in_category:
            if item.condition > best_condition:
                best_condition = item.condition
                winner = item
        return winner

    def swap_best_by_category(self, other, my_priority, their_priority):
        other_best = other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        if other_best and my_best:
            self.add(other_best)
            other.remove(other_best)
            other.add(my_best)
            self.remove(my_best)
            return True
        else:
            return False

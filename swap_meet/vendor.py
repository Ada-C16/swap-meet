class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return self.item

    def remove(self, item):
        self.item = item
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        items_in_inventory = []
        self.category = category
        for self.item in self.inventory:
            if self.item.category == self.category:
                items_in_inventory.append(self.item)
        return items_in_inventory

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            first_item = self.inventory[0]
            other_first_item = other_vendor.inventory[0]
            self.inventory.remove(first_item)
            self.inventory.append(other_first_item)
            other_vendor.inventory.remove(other_first_item)
            other_vendor.inventory.append(first_item)
        return True


    def get_best_by_category(self, category):
        items_in_matching_category = []
        self.category = category

        for item in self.inventory:
            if item.category == category:
                items_in_matching_category.append(item)
        if not items_in_matching_category:
            return None

        current = items_in_matching_category[0]
        for item in items_in_matching_category:
            if item.condition > current.condition:
                current = item
        return current

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if not my_item or not their_item:
            return False
        else:
            return self.swap_items(other, my_item, their_item)
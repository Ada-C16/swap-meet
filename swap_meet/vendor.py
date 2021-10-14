class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        result = self.inventory.pop(self.inventory.index(item))
        return result
        
    def get_by_category(self, category_name):
        category = []
        if not category_name:
            return category

        for i in self.inventory:
            if category_name == i.category:
                category.append(i)

        return category

    def swap_items(self, vendor, my_item, their_item):
        other_vendor = vendor

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        their_swap = other_vendor.remove(their_item)
        my_swap = self.remove(my_item)

        self.add(their_swap)
        other_vendor.add(my_swap)

        return True

    def swap_first_item(self, vendor):
        other_vendor = vendor

        if not self.inventory or not other_vendor.inventory:
            return False

        first_result = self.inventory.pop(0)
        thier_first = other_vendor.inventory.pop(0)

        self.add(thier_first)
        other_vendor.add(first_result)

        return True
        

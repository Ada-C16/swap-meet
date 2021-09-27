class Vendor:
    
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False

    def get_by_category(self, category):
        result = []
        for thing in self.inventory:
            if thing.category == category:
                result.append(thing)
        return result

    def swap_items(self, other_vendor, self_item, other_vendor_item):
        if self_item in self.inventory and other_vendor_item in other_vendor.inventory:
            self.inventory.append(other_vendor_item)
            other_vendor.inventory.remove(other_vendor_item)
            other_vendor.inventory.append(self_item)
            self.inventory.remove(self_item)
            return True
        else:
            return False
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) >= 1 and len(other_vendor.inventory) >= 1:
            self.inventory.append(other_vendor.inventory[0])
            other_vendor.inventory.remove(other_vendor.inventory[0])
            other_vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            return True
        else:
            return False

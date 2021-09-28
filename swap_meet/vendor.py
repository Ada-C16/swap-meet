class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
        except:
            return False
        return item

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]
    
    def swap_items(self, other_vendor, item_to_give, item_to_receive):
        if item_to_give not in self.inventory or item_to_receive not in other_vendor.inventory:
            return False
        self.inventory.remove(item_to_give)
        other_vendor.inventory.append(item_to_give)
        self.inventory.append(item_to_receive)
        other_vendor.inventory.remove(item_to_receive)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        item_to_give = self.inventory.pop(0)
        other_vendor.inventory.append(item_to_give)
        item_to_receive = other_vendor.inventory.pop(0)
        self.inventory.append(item_to_receive)
        return True

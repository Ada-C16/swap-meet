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

        return False

    def get_by_category(self, category):
        item_in_category = []
        for item in self.inventory:
            if item.category == category:
                item_in_category.append(item)
        
        return item_in_category

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        self.add(their_item)
        vendor.add(my_item)
        self.remove(my_item)
        vendor.remove(their_item)
        
        return True

    def swap_first_item(self, vendor_friend):
        if not self.inventory or not vendor_friend.inventory:
            return False
        
        vendor_friend.inventory.append(self.inventory[0])
        self.inventory.pop(0)
        self.inventory.append(vendor_friend.inventory[0])
        vendor_friend.inventory.pop(0)

        return True





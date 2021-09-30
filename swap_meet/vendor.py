from swap_meet.item import Item
# wave 1
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


    


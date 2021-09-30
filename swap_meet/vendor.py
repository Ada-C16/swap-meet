class Vendor:
    def __init__(self,inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
        # if inventory != None else inventory = []
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
        result = []
        for each in self.inventory:
            if each.category == category:
                result.append(each)
        return result
    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            vendor.inventory.remove(their_item)
            vendor.inventory.append(my_item)
            return True
        else:
            return False
    def swap_first_item(self, vendor):
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
            self.inventory.append(vendor.inventory[0])
            vendor.inventory.append(self.inventory[0])
            self.inventory.pop(0)
            vendor.inventory.pop(0)
            return True
        else:
            return False        
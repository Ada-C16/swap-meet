class Vendor:
    def __init__(self, inventory=[]):
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

    def get_by_category (self, category):
        list_of_items = []
        for item in self.inventory:
            if item.category == category:
                list_of_items.append(item)
        return list_of_items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            vendor.add(my_item)
            vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False
    #not working        
    def swap_first_item(self, vendor):
        if vendor.inventory and self.inventory:
            friends_first_item = vendor.inventory.remove(vendor.inventory[0])
            my_first_item = self.inventory.remove(self.inventory[0])
            vendor.inventory.append(my_first_item) 
            self.inventory.append(friends_first_item) 
            return True
        else:
            return False
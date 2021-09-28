class Vendor():
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

    def get_by_category(self, category_string):
        list_by_category =[]
        for item in self.inventory:
            if item.category == category_string:
                list_by_category.append(item)
        return list_by_category

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if len(self.inventory)> 1 and len(vendor.inventory)> 1:
            my_first_item = self.inventory[0]
            their_first_item = vendor.inventory[0]
            self.inventory.remove(my_first_item)
            self.inventory.append(their_first_item)
            vendor.inventory.remove(their_first_item)
            vendor.inventory.append(my_first_item)
            return True
        else:
            return False

            






from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory= None):
        if not inventory:
            inventory = []
        self. inventory = inventory
        #self.item = Item()

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
#Wave 2
    def get_by_category(self, category):
        items = []
        for x in self.inventory:
            if x.category == category:
                items.append(x)
            
        return items
#Wave 3
    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item  in vendor.inventory:
            self.inventory.append(their_item)
            vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            vendor.inventory.remove(their_item)
            return True

        return False

#Wave 4 
    def swap_first_item(self, vendor):

        if self.inventory and vendor.inventory:
            my_item = self.inventory[0]
            their_item = vendor.inventory[0]
            self.inventory.append(their_item)
            vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            vendor.inventory.remove(their_item)
            return True

        return False

#Wave 5
    







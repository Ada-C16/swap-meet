from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory= None):
        if not inventory:
            inventory = []
        self. inventory = inventory
        #self.item = Item()

    def add(self, item):
        #Here Vendor becomes a composite and item becomes a component
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

#Wave 6
    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        if not category_items:
            return None
        best_item = category_items[0]
        for item in category_items:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if not my_best_item or not their_best_item:
            return False
        self.swap_items(other, my_best_item, their_best_item)
        return True

    







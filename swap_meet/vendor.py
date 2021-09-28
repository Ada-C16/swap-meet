
class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
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

    def get_inventory(self):
        return self.inventory

    def get_by_category(self, category = ""):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)        
        return items

    def swap_items(self, vendor, my_item, their_item):

        #helper function for this condition?
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)

            return True
        else:
            return False
    
    #maybe there can be a helper function that does the swapping portion for us. 
    #We can send it the items and have it swap them, you can optionally send it position too?
    def swap_first_item(self, vendor_friend):
        if len(self.inventory) == 0 or len(vendor_friend.inventory) == 0:
            return False
        else:
            my_item = self.inventory[0]
            their_item = vendor_friend.inventory[0]
            self.inventory[0] = their_item
            vendor_friend.inventory[0] = my_item
            return True





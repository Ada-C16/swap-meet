from swap_meet.item import Item

class Vendor():
    def __init__(self, inventory=None):
        if not inventory: #if not None
            inventory = []
        #instantiate attributes
        self.inventory = inventory
        self.item = Item()


    #adds item to inventory list
    def add(self, item):
        self.inventory.append(item)
        return item


    #removes item from inventory list
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item


    #return inventory list with given category
    def get_by_category(self, category):
        inventory_category = []

        #loop through each item in inventory and add item
        #if item category matches given category
        for self.item in self.inventory:
            if self.item.category == category:
                inventory_category.append(self.item)
        return inventory_category


    def swap_items(self, other_vendor, my_item=None, their_item=None):
        #if any items are None, return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
    
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True
            


    # def swap_first_ten_items(self,
    #                         other_vendor,
    #                         inventory[0],
    #                         other_vendor.inventory[0]):
    
    #     pass

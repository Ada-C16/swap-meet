from .item import Item

class Vendor():
    def __init__(self, inventory=None):
        if not inventory: #if not None
            inventory = []
        #instantiate attributes
        self.inventory = inventory


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
        for item in self.inventory:
            if item.category == category:
                inventory_category.append(item)
        return inventory_category


    #swap given items if items are not in designated inventories
    def swap_items(self, other_vendor, my_item=None, their_item=None):
        #if any items are in designated inventory, return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
    
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True


    #returns True/False if inventories are not empty
    def swap_first_item(self, other_vendor):
        if self.inventory or other_vendor.inventory:
            return False

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

    #returns item with the best condition in given category
    def get_best_by_category(self, category):
        category_list = []

        #if inventory is not False, return None
        if self.inventory==[]:
            return None

        #iterate through self.inventory
            #checks for self.condition and matching category
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        
        #returns max condition
        if category_list==[]:
            return None
        
        return max(category_list, key=lambda item : item.condition)


    
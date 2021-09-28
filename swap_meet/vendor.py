#WAVE 01
# [X] For Tests 1-2 
#     [X] Each Vendor will have an attribute named 
#         inventory, which is an empty list by default
#     [X] When we create initialize an instance of Vendor, 
#         we can optionally pass in a list with the keyword 
#         argument inventory
# [ ] For Tests 3-5
#     [X] Every instance of Vendor has an instance method 
#         named add, which takes in one item 
#     [X] This method adds the item to the inventory 
#     [X] This method returns the item that was added
#     [X] Similarly, every instance of Vendor has an instance 
#         method named remove, which takes in one item
#     [X] This method removes the matching item from the inventory
#     [X] This method returns the item that was removed
#     [X] If there is no matching item in the inventory, the method 
#         should return False

class Vendor:
    def __init__ (self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    
    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item

    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else: 
            return False
        
    def get_by_category(self, category):
        category_inventory = []
        for item in self.inventory:
            if item.category == category:
                category_inventory.append(item)
        return category_inventory
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        else:
        #remove my_item from self.inventory, add it to other_vendor.inventory 
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            #remove their_item from other_vendor.inventory, add it to self.inventory
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
        return True




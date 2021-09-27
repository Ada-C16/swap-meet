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
#     [ ] This method removes the matching item from the inventory
#     [ ] This method returns the item that was removed
#     [ ] If there is no matching item in the inventory, the method 
#         should return False


class Vendor:
    def __init__ (self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, add_item):
        #add item from inventory list
        self.inventory.append(add_item)
        #return added item
        return add_item

    def remove(self, remove_item):
        #if remove item in inventory list
        if remove_item in self.inventory:
            #remove item from inventory list
            self.inventory.remove(remove_item)
            #return removed item
            return remove_item
        #otherwise return False
        else: 
            return False




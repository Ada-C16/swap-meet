from swap_meet import item
from swap_meet.item import Item

class Vendor:
    # Vendor class takes in a list that represents a vendor's inventory items.
    # If nothing is passed in, an empty list is created
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        
        self.inventory = inventory

    # instance method takes an item, appends to inventory list, and returns item
    def add(self, item):
        self.inventory.append(item)
        return item

    # instance method removes item from inventory list, and returns item
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    # sorts inventory items to only return items of a given category
    def get_by_category(self, category):
        items_by_category = []
        for item in self.inventory: # loop through each item in vendor's inventory
            if item.category == category: # if item at iteration matches the category we want,
                items_by_category.append(item) # append to items_by_category list

        return items_by_category

    # other is an instance of Vendor class
    # instance method takes other, an item the vendor wants to swap, and an item that other wants to swap
    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory and their_item in other.inventory:
            other.add(my_item) # add vendor item to other's inventory,
            self.remove(my_item) # remove vendor item from inventory
            self.add(their_item) # add other's item to vendor inventory
            other.remove(their_item) # remove other's item from other's inventory
            return True
        return False

    # swaps only the first items in vendor's inventory and other's inventory
    def swap_first_item(self, other):
        if self.inventory and other.inventory:
            my_first_item = self.inventory[0]
            their_first_item = other.inventory[0]

            self.swap_items(other, my_first_item, their_first_item)

            return True
        return False

    # gets the item with the best condition in a certain category 
    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category) # assigns reference to vendor's items of a certain category, using get_by_category instance method
        highest_condition = 0
        best_item = ""

        if items_by_category:
            for item in items_by_category:
                if item.condition > highest_condition: # only enter if clause if current item's condition is greater than highest_condition
                    best_item = item # if the condition is higher, best_item is now the current item
                    highest_condition = item.condition # highest_condition gets updated to equal the current item's condition
            return best_item
        return None

    # swaps the best item of a certain category with other, an instance of Vendor
    # uses get_best_by_category instance method to determine items of highest quality, of certain category
    # then swaps (Vendor receives other's item, other receives vendor's item) using swap_items method
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if my_best_item in self.get_by_category(their_priority) and their_best_item in other.get_by_category(my_priority):
            self.swap_items(other, my_best_item, their_best_item)
            return True
        return False
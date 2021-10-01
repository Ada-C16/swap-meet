# from .item import Item
# from .clothing import Clothing
# from .decor import Decor
# from .electronics import Electronics


class Vendor:
    """
    Vendor class has an attribute called inventory which by default an empty list
    Wave 1:
    It has a add method that add item into inventory list
    It has a remove method that removes duplicate items from inventory list 
    Wave 2: 
    It has a get_by_category that returns list of items w/same category
    Wave 3: 
    It as a swap_items which allows the vendor and their friend to swap items
    """
    # ********* Wave 1 **********

    # initalize the constructor and set inventory to None
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    # this function adds item into inventory and return added item
    def add(self, item):

        self.inventory.append(item)
        return item

    # this function removes duplicate items from list and return duplicate item
    # else return False if no item in list
    def remove(self, item):
        for i in self.inventory:
            if i == item:
                self.inventory.remove(i)
                return i

        return False

    # ********* Wave 2 **********

    # this function returns a list of items with same category
    def get_by_category(self, category):
        same_category = []
        for item in self.inventory:  # item is an instance of the Item
            if item.category == category:
                same_category.append(item)

        return same_category

    # ********* Wave 3 **********

    def swap_items(self, friend_vendor, my_item, friend_item):

        """
        This function takes in 3 arguments:
            friend_vendor - Vendor's class object
            my_item - Item's class object
            friend_item - Item's class object
        """

        # if neither vendor or friend_vendor contain the item return false
        if not self.contains(my_item) or not friend_vendor.contains(friend_item):
            return False

        # remove my_item and append to friend_vendor
        self.remove(my_item)
        friend_vendor.add(my_item)

        # remove friend_item from list and append to inventory
        friend_vendor.remove(friend_item)
        self.add(friend_item)

        return True

    # this function checks to see if item is in list, return boolean
    def contains(self, item):
        return item in self.inventory

    # ********* Wave 4 **********

    def swap_first_item(self, friend_vendor):

        """
        -Remove first item from inventory and append to friend's inventory
        -Remove friend's first item and append to vendor's inventory
        -If either list is empty return False
        """
        
        if len(self.inventory) == 0 or len(friend_vendor.inventory) == 0:
            return False

        # pop returns the item that it removed
        vendor_first_item = self.inventory.pop(0)
        friend_vendor.inventory.append(vendor_first_item)

        friend_first_item = friend_vendor.inventory.pop(0)
        self.inventory.append(friend_first_item)

        return True

    # ********* Wave 6 **********

    def get_best_by_category(self, item_category):
        """
        -item_category: a string that represents a category
        -get item with best conditions
        -checking for highest condtion and matching category and return item
        -if no item matches category return None
        -return single item even if there are duplicates items & conditions
        """

        result = []
        for item in self.inventory:
            if item.category == item_category:
                result.append(item)

        highest_condition = -1
        highest_condition_item = None
        for item in result:
            if item.condition > highest_condition:
                highest_condition = item.condition
                highest_condition_item = item

        return highest_condition_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        -other: another vendor's instance
        -my_priority: a category that the vendor wants to receive
        -their_priority: a category that other wants to receive

        Return True:
        -best item in my inventory that matches their_priority category is swapped
        with the best item in other's inventory that matches my_priority

        Return False:
        -If the Vendor has no item that matches their_priority category,
        swapping does not happen, and it returns False
        -If other has no item that matches my_priority category, 
        swapping does not happen, and it returns False
        """

        best_item_in_my_inventory = self.get_best_by_category(their_priority)

        best_item_in_other_inventory = other.get_best_by_category(my_priority)

        return self.swap_items(other, best_item_in_my_inventory, best_item_in_other_inventory)

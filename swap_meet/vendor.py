from swap_meet.item import Item


class Vendor:
    """
    This class has one attribute, inventory, which is an empty list by default. 
    Inventory can optionally taken in an 'inventory' argument.
    This class has two methods: add() and remove().
    Both methods will take in one argument, item. The add method will append the item to 
    the list and return item. Remove will remove the item from list and return item.
    """

    def __init__(self, inventory=None):

        self.inventory = inventory if inventory is not None else []
        self.category_list = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        # return list of item with
        for item in self.inventory:
            if item.category == category:
                self.category_list.append(item)
        return self.category_list

    def swap_items(self, friend_vendor, my_item, their_item):
        """
        Takes in three arguments: friend_vendor, my_item, and their_item.
        friend_vendor is an instance of Vendor class, my_item and their_item
        are instances of Item class. If my_item not in inventory or their_item
        not in friend_vendor inventory, return False. Otherwise, remove the item from
        the original inventory and add it to the others' inventory.
        """

        if their_item not in friend_vendor.inventory or \
                my_item not in self.inventory:
            return False

        friend_vendor.add(my_item)
        self.add(their_item)
        friend_vendor.remove(their_item)
        self.remove(my_item)

        return True

    def swap_first_item(self, friend_vendor):
        """
        This function has one parameter, an instance of Vendor class 
        for their friend_vendor. If either the self inventory or friend's inventory
        is empty, we return False. Otherwise, we take the first item from the self
        inventory and add it to friend_vendor inventory. We take the first item from 
        friend_vendor inventory and add it to self inventory.
        """
        if self.inventory == [] or friend_vendor.inventory == []:
            return False

        self.add(friend_vendor.inventory[0])
        friend_vendor.add(self.inventory[0])

        self.inventory.remove(self.inventory[0])
        friend_vendor.inventory.remove(friend_vendor.inventory[0])
        
        return True

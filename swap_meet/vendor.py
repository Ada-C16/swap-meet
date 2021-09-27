from typing import ItemsView
from swap_meet.item import Item

class Vendor:
    """
    Attributes:: 
    inventory: an empty list by default, 
    optionally can pass in a list

    Ins. methods::
    add : takes in one item and adds it to the inventory
    returns the item that was added

    remove: takes in an item and removes it from inventory
    returns the item removed

    if no matching item in the inventory return false
    """

    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        items_in_category = []

        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)

        return items_in_category

    def swap_items(self, friend, my_item, their_item):

        if not my_item in self.inventory or not their_item in friend.inventory:
            return False

        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        friend.inventory.remove(their_item)
        friend.inventory.append(my_item)
        return True

    
    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False

        my_first_item = self.inventory[0]
        their_first_item = friend.inventory[0]

        self.inventory.remove(my_first_item)
        self.inventory.append(their_first_item)

        friend.inventory.remove(their_first_item)
        friend.inventory.append(my_first_item)

        return True
    
    
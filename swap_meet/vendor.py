from swap_meet.item import Item


class Vendor:
    """
    This class has one attribute, inventory, which is an empty list by default. 
    Inventory can optionally taken in an 'inventory' argument.
    This class has multiple methods to track and change the state of items in
    a vendor's inventory at a swap meet.
    """

    def __init__(self, inventory=None):

        self.inventory = inventory if inventory is not None else []
        self.category_list = []

    def add(self, item):
        """
        Takes item in as argument and adds the item to the inventory. Returns item.
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        Takes item as argument and removes item from inventory. Returns item.
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        """
        Takes in a string, category, and searches for item with that category attribute.
        Returns list of items with category attribute.
        """
        for item in self.inventory:
            if item.category == category:
                self.category_list.append(item)
        return self.category_list

    def swap_items(self, friend_vendor, my_item, their_item):
        """
        Takes in three arguments: friend_vendor: Vendor, my_item: Item, and their_item: Item.
        Remove item from original inventory and add to the others' inventory. Else, return False
        """

        if their_item not in friend_vendor.inventory or \
                my_item not in self.inventory:
            return False

        friend_vendor.add(my_item)
        self.add(their_item)

        return friend_vendor.remove(their_item), self.remove(my_item)

    def swap_first_item(self, friend_vendor):
        """
        Takes in one argument: friend_vendor
        If self.inventory or friend_vendor.inventory is empty, return False. 
        Else, remove first items from original inventories and add them the other inventory. 
        Return True
        """

        if self.inventory == [] or friend_vendor.inventory == []:
            return False
        else:
            my_item = self.inventory[0]
            their_item = friend_vendor.inventory[0]

        return self.swap_items(friend_vendor, my_item, their_item)

    def get_best_by_category(self, category):
        """
        Takes in one parameter, category. Returns all items with the highest condition value.
        Returns None if no item matching category in inventory
        """
        self.best_category = self.get_by_category(category)

        items_condition_list = []
        for item in self.best_category:
            if item:
                items_condition_list.append(item.condition)
                if items_condition_list != False:
                    best_item = max(items_condition_list)
            else:
                return None
        for item in self.best_category:
            if item.condition == best_item:
                return item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Like swap_items but by the best category
        """
        if not self.get_best_by_category(their_priority) and (
                other.get_best_by_category(my_priority)):
            return False
        else:
            what_self_wants = other.get_best_by_category(my_priority)
            what_they_want = self.get_best_by_category(their_priority)

        return self.swap_items(other, what_they_want, what_self_wants)

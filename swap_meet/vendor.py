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
        If my_item not in inventory or their_item not in friend_vendor inventory, return False. 
        Else, remove item from original inventory and add it to the others' inventory.
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
        Takes in one argument: friend_vendor
        If self.inventory or friend_vendor.inventory is empty, return False. 
        Else, remove first items from original inventories and add them the other inventory. 
        Return True
        """
        if self.inventory == [] or friend_vendor.inventory == []:
            return False

        self.add(friend_vendor.inventory[0])
        friend_vendor.add(self.inventory[0])

        self.inventory.remove(self.inventory[0])
        friend_vendor.inventory.remove(friend_vendor.inventory[0])

        return True

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
        Takes in three parameters: other for other vendor, my_priority for category self wants
        and their_priority for category other wants.
        Returns False if my_priority or their_priority is not present in the other's inventory.
        Else, best my_priority and best their_priority item from original inventory and swaps
        them into other vendor's inventory.
        """
        self.other = other
        self.my_priority = my_priority
        self.their_priority = their_priority

        # looks for their priority in self inventory
        if self.get_best_by_category(self.their_priority) == None:
            return False
        # looks for my priority in other inventory
        elif self.other.get_best_by_category(self.my_priority) == None:
            return False
        else:
            what_self_wants = self.other.get_best_by_category(self.my_priority)
            what_they_want = self.get_best_by_category(self.their_priority)
            self.swap_items(self.other, what_they_want, what_self_wants)
            return True

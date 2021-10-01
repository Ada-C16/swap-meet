from swap_meet.item import Item


class Vendor:
    """
    Has one attribute, parameter, which is an empty list by default. 
    Has multiple methods to track and change items in a vendor's inventory
    """

    def __init__(self, inventory=None):

        self.inventory = inventory if inventory is not None else []
        self.category_list = []
        self.age_list = []

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
        self.category_list = [
            item for item in self.inventory if item.category == category]

        return self.category_list

    def swap_items(self, friend_vendor, my_item, their_item):
        """
        Takes in three arguments: friend_vendor: Vendor, my_item: Item, and their_item: Item.
        Remove item from original inventory and add to the others' inventory. Else, return False
        """
        if not (their_item in friend_vendor.inventory and
                my_item in self.inventory):
            return False
        friend_vendor.add(my_item) and self.add(their_item)

        return friend_vendor.remove(their_item), self.remove(my_item)

    def swap_first_item(self, friend_vendor):
        """
        If self.inventory/friend_vendor.inventory is empty, return False. 
        Remove first items from original inventories and add to  other inventory. Return True
        """
        if not (self.inventory and friend_vendor.inventory):
            return False

        return self.swap_items(friend_vendor, self.inventory[0], friend_vendor.inventory[0])

    def get_best_by_category(self, category):
        """
        Like get_by_category but searches for best/max condition
        """
        self.best_category = self.get_by_category(category)
        best_item = None
        best_condition = 0
        for item in self.best_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Swaps items by the best category
        """
        if not self.get_best_by_category(their_priority) and (
                other.get_best_by_category(my_priority)):
            return False
        else:
            what_self_wants = other.get_best_by_category(my_priority)
            what_they_want = self.get_best_by_category(their_priority)

        return self.swap_items(other, what_they_want, what_self_wants)

    def get_by_age(self, age):
        """
        Returns a specific item by the desired age passed in as argument
        """
        for item in self.inventory:
            if item.age == age:
                self.age_list.append(item)
                return item

    def get_by_newest(self):
        """
        Returns item of the lowest, valid range
        """
        min_age = min([item.age for item in self.inventory])
        for item in self.inventory:
            if item.age == min_age:
                return item

    def swap_by_newest(self, other):
        """
        Vendor and other vendor will swap their newest items with each other.
        """
        their_newest = other.get_by_newest()
        my_newest = self.get_by_newest()

        return self.swap_items(other, my_newest, their_newest)

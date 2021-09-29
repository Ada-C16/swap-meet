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

    def get_best_by_category(self, category):
        self.best_category = self.get_by_category(category)

        items_condition_list = []
        for item in self.best_category:
            items_condition_list.append(item.condition)
            if items_condition_list != False:
                best_item = max(items_condition_list)
        for item in self.best_category:
            if item.condition == best_item:
                return item
        if self.get_by_category(category) == False:
            return None

    # def swap_best_by_category(self, other_vendor, my_priority,their_priority):
    #     self.other = other_vendor
    #     self.my_priority = my_priority
    #     self.their_priority = their_priority
    #     self.default_condition = 0
    #     self.their_default_condition = 0

    #     if self.their_priority not in self.inventory:
    #         return False
    #     if self.my_priority not in self.other:
    #         return False
    #     else:
    #         for item in self.inventory:
    #             if item.category == their_priority:
    #                 if item.condition_description > self.default_condition:
    #                     self.default_condition = item.condition_description
    #         for item in self.other.inventory:
    #             if item.category == my_priority:
    #                 if item.condition_description > self.their_default_condition:
    #                     self.their_default_condition = item.condition_description
    #         self.inventory.remove(self.default_condition)
    #         self.inventory.add(self.their_default_condition)
    #         self.other.inventory.remove(self.their_default_condition)
    #         self.other.inventory.add(self.default_condition)
    #         return True

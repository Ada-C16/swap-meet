from typing import ItemsView

class Vendor:

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

    def swap_items(self, other, my_item, their_item):

        if not my_item in self.inventory or not their_item in other.inventory:
            return False

        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        other.inventory.remove(their_item)
        other.inventory.append(my_item)
        return True

    
    def swap_first_item(self, other):
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False

        my_first_item = self.inventory[0]
        their_first_item = other.inventory[0]

        self.swap_items(other, my_first_item, their_first_item)

        return True
    
    def get_best_by_category(self, category):
        list_of_items_in_category = self.get_by_category(category)
        
        if len(list_of_items_in_category) == 0:
            return None

        item_highest_condition = ("", 0)
        for item in list_of_items_in_category:
            if item.condition > item_highest_condition[1]:
                item_highest_condition = (item, item.condition)
        return item_highest_condition[0]

    def swap_best_by_category(self, other, my_priority,their_priority):

        my_best_item_their_priority = self.get_best_by_category(their_priority)
        their_best_item_my_priority = other.get_best_by_category(my_priority)
        if not my_best_item_their_priority or not their_best_item_my_priority:
            return False
        self.swap_items(other, my_best_item_their_priority, their_best_item_my_priority)

        return True 

    def swap_by_newest(self, other):

        my_newest = ("",)
        their_newest = ("",)
        
        for item in self.inventory:
            if item.age > my_newest[1]:
                my_newest = (item, item.age)

        for item in other.inventory:
            if item.age > their_newest[1]:
                their_newest = (item, item.age)

        self.swap_items(other, my_newest, their_newest)

        return True
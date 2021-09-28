from swap_meet import item
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        items_by_category = []
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)

        return items_by_category

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            friend.remove(their_item)
            return True
        return False

    def swap_first_item(self, other):
        if self.inventory and other.inventory:
            my_first_item = self.inventory[0]
            their_first_item = other.inventory[0]

            self.swap_items(other, my_first_item, their_first_item)

            return True
        return False

    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category)
        highest_condition = 0
        best_item = ""

        if items_by_category:
            for item in items_by_category:
                if item.condition > highest_condition:
                    best_item = item
                    highest_condition = item.condition
            return best_item
        return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if my_best_item in self.get_by_category(their_priority) and their_best_item in other.get_by_category(my_priority):
            self.swap_items(other, my_best_item, their_best_item)
            return True
        return False
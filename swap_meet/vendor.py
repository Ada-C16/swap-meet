from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
    
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
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        
        return category_items
    
    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.remove(my_item)
            friend.remove(their_item)
            friend.add(my_item)
            self.add(their_item)
            return True
        else:
            return False

    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True

    def get_best_by_category(self, category):
        matching_category = self.get_by_category(category)
        if matching_category == []:
            return None
        
        best_condition = 0
        best_item = None

        for item in matching_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        best_item_for_them = self.get_best_by_category(their_priority)
        best_item_for_me = other.get_best_by_category(my_priority)
        
        if best_item_for_them is None or best_item_for_me is None:
            return False
        else:
            self.swap_items(other, best_item_for_them, best_item_for_me)
            return True
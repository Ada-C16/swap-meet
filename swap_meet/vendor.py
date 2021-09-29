from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
    
    def add_item(self, item):
        self.inventory.append(item)
        return item
    
    def remove_item(self, item):
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
            self.inventory.remove_item(my_item)
            friend.inventory.remove_item(their_item)
            friend.inventory.add_item(my_item)
            self.inventory.add_item(their_item)
            return True
        else:
            return False

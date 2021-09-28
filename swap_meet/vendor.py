from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

    def add(self, item):
        item = Item()
        self.inventory.append(item)
        return item

    def remove(self, item):
        item = Item()
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False 

    def get_by_category(self, category):
        items_by_category =[]
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)
        
        return items_by_category

    def swap_items(self, friend, my_item, their_item):

        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.remove(my_item)
            friend.inventory.remove(their_item)
            friend.inventory.append(my_item)
            self.inventory.append(their_item)
            return True
        else:
            return False



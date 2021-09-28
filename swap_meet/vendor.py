from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items = []

        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, swapee, my_item, their_item):
        if my_item in self.inventory and their_item in swapee.inventory:
            swapee.add(my_item)
            self.add(their_item)
            swapee.remove(their_item)
            self.remove(my_item)
            return True
        return False

    def swap_first_item(self, swapee):
        if self.inventory and swapee.inventory:
            my_item = self.inventory[0]
            their_item = swapee.inventory[0]
            
            self.add(their_item)
            swapee.add(my_item)
            self.remove(my_item)
            swapee.remove(their_item)
            return True
        return False

    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        
        if not category_items:
            return None
        
        best_item = category_items[0]
        for item in category_items:
            if item.condition > best_item.condition:
                best_item = item
        
        return best_item

    
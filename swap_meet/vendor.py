from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory: 
            inventory = []
        self.inventory = inventory # list of items

    # Adding item to inventory.
    def add(self, item):
        self.inventory.append(item)
        return item
    
    # Removing item from inventory. 
    # Returning false if not in inventory.
    def remove(self, item): 
        if item not in self.inventory:
            return False 
        self.inventory.remove(item)
        return item
    
    # Returning items within a given category
    def get_by_category(self, category):
        category_items_list = []

        for item in self.inventory: 
            if item.category == category:
                category_items_list.append(item)
        
        return category_items_list

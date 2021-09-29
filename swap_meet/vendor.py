from .item import Item

class Vendor:
    def __init__(self, inventory=None, category=""):
        if not inventory:
            inventory = []
        self.inventory = inventory
        self.category = category
    
    def add(self, item_add):
        self.inventory.append(item_add)
        return item_add

    def remove(self, item_remove):
        if item_remove not in self.inventory:
            return False
        self.inventory.remove(item_remove)
        return item_remove

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list
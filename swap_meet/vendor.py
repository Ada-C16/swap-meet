from .item import Item

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        updated_inventory = self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            updated_inventory = self.inventory.remove(item)
        else: 
            item = False
        return item

    def get_by_category(self, category):
        items = []
        # [items.append(item) for item in self.inventory if item.category == category]
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
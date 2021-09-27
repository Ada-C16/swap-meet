from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            removed_item = self.inventory.pop()
            return removed_item
        else:
            return False
    
    def get_by_category(self, category):
        pass

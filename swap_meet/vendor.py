from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory: 
            inventory = []
        self.inventory = inventory
        self.item = Item()


    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        items = []
        
        for item in self.inventory:
            if item.category == category:
                items.append(item)
                
        return items
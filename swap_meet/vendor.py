from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[], item=None):
        self.inventory = inventory
        self.item = item


    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            removed_item = self.inventory.pop()
            return removed_item
        else:
            return False
    
    def get_by_category(self, category=''):
        categories_present_list = []
        for i in range(len(self.inventory)):
            if category == self.inventory[i].category: 
                categories_present_list.append(self.inventory[i])
            else:
                continue
        return categories_present_list
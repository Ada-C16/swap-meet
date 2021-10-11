from swap_meet.item import Item 

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory 

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
        '''This method returns a list of Item`s in the 
        inventory with that category'''
        inventory_list = []
        for item in self.inventory: 
            if item.category == category:
                inventory_list.append(item)
        return inventory_list 

class Vendor:
    def __init__(self, inventory = list()):
        if not inventory:
            inventory = []
        self.inventory = inventory
   
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return None
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        item_list = [] 
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        
        return item_list

    def swap_items(self, friend_inv, this_item, their_item):
        if not this_item and not their_item:
            return False
        self.inventory.remove(this_item)
        friend_inv.inventory.append(this_item)
        friend_inv.inventory.remove(their_item)
        self.inventory.append(their_item)

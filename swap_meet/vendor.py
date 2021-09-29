class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

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
        items_in_category = []
        for item in self.inventory:
            if item.category == category:  
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            return True
        else:
            return False
    
    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True
        else:
            return False

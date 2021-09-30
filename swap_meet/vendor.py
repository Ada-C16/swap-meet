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

    def swap_items(self, friend, my_item, their_item):
        if their_item not in friend.inventory or my_item not in self.inventory:
            return False
        self.inventory.remove(my_item)
        friend.inventory.append(my_item)
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True

    def swap_first_item(self, friend):
        if self.inventory == [] or friend.inventory == []:
            return False
        my_first_item = self.inventory[0]
        their_first_item = friend.inventory[0]
        friend.inventory.append(my_first_item)
        self.inventory.remove(my_first_item)
        self.inventory.append(their_first_item)
        friend.inventory.remove(their_first_item)
        
        return True

from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return not item
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, one_category):
        items= [item for item in self.inventory if item.category == one_category]
        return items

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        else:
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            friend.inventory.append(my_item)
            self.inventory.remove(my_item)
            return True
    
    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        
        else:
            self.inventory.append(friend.inventory[0])
            friend.inventory.append(self.inventory[0])
            self.inventory.pop(0)
            friend.inventory.pop(0)
            return True




from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        result = item
        self.inventory.append(result)
        return result
    
    def remove(self, item):
        result = item
        if item in self.inventory:
            self.inventory.remove(result)
        else:
            return False
        return result

    def get_by_category(self, category):
        items_by_category = []
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)
        return items_by_category

    def swap_items(self, friend, my_item, their_item):
        if not self.remove(my_item):
            return False
        if not friend.remove(their_item):
            self.add(my_item)
            return False
        self.add(their_item)
        friend.add(my_item)
        return True

    def swap_first_item(self,friend):
        if len(self.inventory) > 0 and len(friend.inventory) > 0:
            return self.swap_items(friend,self.inventory[0],friend.inventory[0])
        return False

    def get_best_by_category(self,category):
        items = Vendor.get_by_category(self,category)
        if len(items) == 0:
            return None
        max_value = 0
        max_item_value = None
        for item in items:
            if item.condition > max_value:
                max_value = item.condition
                max_item_value = item               
        return max_item_value

    def swap_best_by_category(self,other,my_priority,their_priority):
        my_swap = self.get_best_by_category(their_priority)
        their_swap = other.get_best_by_category(my_priority)
        if my_swap and their_swap:
            self.swap_items(other,my_swap,their_swap)
            return True
        return False

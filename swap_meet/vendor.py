from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory else []

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        self.inventory = [item for item in self.inventory if item != item_to_remove]
        return item_to_remove

    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        return items

    def swap_items(self, other, item_to_give, item_to_get):
        if not (item_to_give in self.inventory and item_to_get in other.inventory):
            return False
        
        self.remove(item_to_give)
        self.add(item_to_get)
        other.remove(item_to_get)
        other.add(item_to_give)
        return True
    
    def swap_first_item(self, other):
        if self.inventory and other.inventory:
            return self.swap_items(other, self.inventory[0], other.inventory[0])

        return False

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if not items:
            return None

        best_item = max(items, key = lambda item:item.condition)
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        item_to_give = self.get_best_by_category(their_priority)
        item_to_get = other.get_best_by_category(my_priority)
        if not (item_to_give and item_to_get):
            return False

        return self.swap_items(other, item_to_give, item_to_get)
    
    def get_newest(self):
        if not self.inventory:
            return None
        return min(self.inventory, key = lambda item:item.age)

    def swap_by_newest(self, other):
        item_to_give = self.get_newest()
        item_to_get = other.get_newest()
        return self.swap_items(other, item_to_give, item_to_get)

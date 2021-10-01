from swap_meet.item import Item


class Vendor():
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []
    def add(self, item):
        self.inventory.append(item)
        return item
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    def get_by_category(self, category):
        things = []
        for item in self.inventory:
            if item.category == category:
                things.append(item)
        return things
    
    def swap_items(self, swapper, my_item, their_item):
        if my_item in self.inventory and their_item in swapper.inventory:
            self.remove(my_item) 
            swapper.add(my_item)
            swapper.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False
    
    def swap_first_item(self, swapper):
        if len(self.inventory) is not 0 and len(swapper.inventory) is not 0:
            thing_one=self.inventory.pop(0)
            thing_two=swapper.inventory.pop(0)
            self.add(thing_two)
            swapper.add(thing_one)
            return True
        else:
            return False
    def get_best_by_category(self, category):
        items_in_category=self.get_by_category(category)
        best_item=Item()
        if len(items_in_category) is 0:
            return None
        else:
            for item in items_in_category:
                if item.condition>best_item.condition:
                    best_item=item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item=self.get_best_by_category(their_priority)
        their_item=other.get_best_by_category(my_priority)
        if my_item is not None and their_item is not None:
            if self.swap_items(other, my_item, their_item) is True:
                return True
        else:
            return False
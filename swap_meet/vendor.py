from swap_meet.item import Item

class Vendor:
    """
    This class has one attribute, inventory, which is an empty list by default. 
    Inventory can optionally taken in an 'inventory' argument.
    This class has two methods: add() and remove().
    Both methods will take in one argument, item. The add method will append the item to 
    the list and return item. Remove will remove the item from list and return item.
    """
    def __init__(self, inventory = []):
        self.inventory = inventory
        self.category_list = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        
    def get_by_category(self, category):
        # return list of item with 
        for item in self.inventory:
            if item.category == category:
                self.category_list.append(item)
        return self.category_list

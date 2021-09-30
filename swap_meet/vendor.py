class Vendor:
    """
    Vendor class for instances of inventory lists
    Inventroy lists are made of instances of the class Item
    Methods include: (add, remove, get_by_category, swap_items, swap_first_item,
    get_best_by_category, swap_best_by_category)
    """

    # class constructor method
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    # add item to vendor list
    def add(self, item):
        self.inventory.append(item)
        return item

    # remove item from vendor list
    def remove(self, item):
        if not item in self.inventory:
            return False

        self.inventory.remove(item)

        return item

    # return list of items by specified category
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)

        return items

    # swap item in vendor list with item in another instance of Vendor
    def swap_items(self, their_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in their_vendor.inventory:
            self.inventory.remove(my_item)
            their_vendor.inventory.append(my_item)
        
            their_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
            
        return False

    # swap the first items in two instances of Vendor
    def swap_first_item(self, their_vendor):
        if not self.inventory or not their_vendor.inventory:
            return False

        self.swap_items(their_vendor, self.inventory[0], their_vendor.inventory[0])

        return True

    # return item in best condition of a specified category
    def get_best_by_category(self, category):        
        items = self.get_by_category(category)

        if items:
            best_condition = items[0]
            for item in items:
                if item.condition > best_condition.condition:
                    best_condition = item
            return best_condition
        else:
            return None

    # swap two items in two instances of Vendor of specified categories with each other
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_by_category = self.get_best_by_category(their_priority)
        their_best_by_category = other.get_best_by_category(my_priority)

        if not my_best_by_category or not their_best_by_category:
            return False
        else:
            self.swap_items(other, my_best_by_category, their_best_by_category)
            return True
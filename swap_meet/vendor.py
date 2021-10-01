class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = [] 
        self.inventory = inventory

    def add(self, add_item):
        self.add_item = add_item
        self.inventory.append(add_item)
        return add_item

    def remove(self, remove_item):
        self.remove_item = remove_item
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        return False

    def get_by_category(self, category_name):
        self.category_name = category_name
        items_list = []
        for item in self.inventory:
            if item.category == category_name:
                items_list.append(item)
        return items_list
            
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
    
        friend.inventory.append(my_item)
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        friend.inventory.remove(their_item)
        return True
    
    def swap_first_item(self, another_vendor):
        if len(another_vendor.inventory) == 0 or len(self.inventory) == 0:
            return False
    
        my_first = self.inventory[0]
        friend_first = another_vendor.inventory[0]

        self.swap_items(another_vendor, my_first, friend_first)
        return True
        
    def get_best_by_category(self, category = ""):

        items_and_category = self.get_by_category(category)

        if len(items_and_category) == 0:
            return None

        return max(items_and_category, key = lambda item : item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_best = self.get_best_by_category(their_priority)
        my_best = other.get_best_by_category(my_priority)
        
        if their_best is None or my_best is None:
            return False
    
        self.swap_items(other, their_best, my_best)
        return True



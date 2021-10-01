class Vendor:

    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, new_item):
        self.new_item = new_item
        self.inventory.append(new_item)
        return new_item

    def remove(self, old_item):
        self.old_item = old_item
        if old_item in self.inventory:
            self.inventory.remove(old_item)
            return old_item
        return False

    def get_by_category(self, category_title): 
        self.category_title = category_title
        clothing_by_category = []
        for item in self.inventory:
            if item.category == category_title:
                clothing_by_category.append(item)
        return clothing_by_category

    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend_vendor.inventory:
            return False
        friend_vendor.inventory.append(my_item)
        self.inventory.remove(my_item)
        self.inventory.append(their_item) 
        friend_vendor.inventory.remove(their_item)    
        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        my_first_item = self.inventory[0]
        other_first = other_vendor.inventory[0]

        self.swap_items(other_vendor, my_first_item, other_first)
        return True 

    def get_best_by_category(self, category_match):
        best_item = None
        best_condition = 0
    
        for item in self.inventory:
            if category_match == item.category and item.condition > best_condition:
                best_condition = item.condition
                best_item = item 
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        if my_best == None or their_best == None:
            return False
        else:
            self.swap_items(other, my_best, their_best)
            return True
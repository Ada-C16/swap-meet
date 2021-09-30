class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory or []

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
        
    def get_best_by_category(self, category):
        '''
        Finds "best" item from items by category based on highest condition rating.
        '''
        return max(self.get_by_category(category), key=lambda item: item.condition, \
            default=None)

    def swap_best_by_category(self, other, my_priority, their_priority):
        if self.get_by_category(their_priority) and other.get_by_category(my_priority):
            self.swap_items(other, self.get_best_by_category(their_priority), \
                other.get_best_by_category(my_priority))
            return True
        else:
            return False

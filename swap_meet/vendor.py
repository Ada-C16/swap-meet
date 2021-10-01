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

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        item_highest_condition=""
        condition_value=0
        if not items_in_category:
            return None
        for item in items_in_category:
            if item.condition > condition_value:
                item_highest_condition=item
                condition_value=item.condition
        return item_highest_condition
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_items_their_priority = self.get_by_category(their_priority)
        their_items_my_priority = other.get_by_category(my_priority)
        if not my_items_their_priority or not their_items_my_priority:
            return False
        else:
            my_highest = self.get_best_by_category(their_priority)
            their_highest = other.get_best_by_category(my_priority)
            
            self.swap_items(other, my_highest, their_highest)
            other.swap_items(other, my_highest, their_highest)
            return True
    

    def swap_by_newest(self):
        pass
        #similar to swap_best_by_category but minus finding best category
        #create function to find the newest, is age number of years? months? 
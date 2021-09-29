from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[], item=None):
        self.inventory = inventory
        self.item = item


    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            removed_item = self.inventory.pop()
            return removed_item
        else:
            return False
    
    def get_by_category(self, category=''):
        categories_present_list = []
        for i in range(len(self.inventory)):
            if category == self.inventory[i].category: 
                categories_present_list.append(self.inventory[i])
            else:
                continue
        return categories_present_list

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            # Remove my_item from MY inventory. 
            # Add removed item to THEIR inventory.
            my_removed_item = self.remove(my_item)
            friend_removed_item = friend.remove(their_item)

            # their_item:
            # Remove an item from THEIR inventory.
            # Add removed item to MY inventory.
            self.add(friend_removed_item)
            friend.add(my_removed_item)
        else:
            # return False if:
            # my_item is not in self.inventory
            # their_item is not in friend's inventory
            return False
        return True
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[], item=None):
        self.inventory = inventory
        self.item = item


    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            for i in range(len(self.inventory)):
                inventory_set = (self.inventory[i], i)
                if item in inventory_set:
                    self.inventory.pop(i)
                    break
            return inventory_set[0]
    
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
            remove_my_item = self.remove(my_item) 
            friend.add(remove_my_item) 

            remove_friend_item = friend.remove(their_item)
            self.add(remove_friend_item)
        else:
            return False
        return True

    def swap_first_item(self, friend):
        for i in range(len(self.inventory)):
            remove_my_item = self.remove(self.inventory[0]) 
            friend.add(remove_my_item) 

            remove_friend_item = friend.remove(friend.inventory[0])
            self.add(remove_friend_item)
            return True
        else:
            return False
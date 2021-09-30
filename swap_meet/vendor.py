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
        if len(self.inventory) > 0 and len(friend.inventory) > 0:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self, category):
        items_matching_category = self.get_by_category(category)
        highest_rated_condition = 0
        highest_rated_item = None

        if len(items_matching_category) == 0:
            return None
        else:
            for i in range(len(items_matching_category)):
                if highest_rated_condition < items_matching_category[i].condition:
                    highest_rated_condition = items_matching_category[i].condition
                    highest_rated_item = items_matching_category[i]
        return highest_rated_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        if len(self.inventory) > 0 and len(other.inventory) > 0:
            my_best_item = self.get_best_by_category(their_priority)
            their_best_item = other.get_best_by_category(my_priority)
            
            if (my_best_item and their_best_item) and (their_priority == my_best_item.category and \
                 my_priority == their_best_item.category):
                self.swap_items(other, my_best_item, their_best_item)
                return True
        else:
            return False
        
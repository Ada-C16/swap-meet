class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item_to_add):
        self.inventory.append(item_to_add)
        return item_to_add
    
    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False 
    
    def get_by_category(self, category):
        items_by_category = []
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)
        return items_by_category 

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or \
            their_item not in friend.inventory:
            return False 
        else: 
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True 

    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False 
        else:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True 

    def get_best_by_category(self, category):
        best_item, rating = "", -1
        for item in self.inventory:
            if item.category == category:
                if item.condition > rating:
                    best_item, rating = item, item.condition

        if best_item == "":
            return None 
        else:
            return best_item 
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = other.get_best_by_category(my_priority)
        their_best_item = self.get_best_by_category(their_priority)

        if my_best_item == None or their_best_item == None:
            return False 
        else:  
            self.swap_items(other, their_best_item, my_best_item)
            return True 

def get_newest_item(self):
    newest_item, age = "", 1000000
    for item in self.inventory:
        if item.age < age:
            newest_item, age = item, item.age 
    
    if newest_item == "":
        return None 
    else:
        return newest_item

def swap_by_newest(self, other):
    my_newest_item = self.get_newest_item()
    their_newest_item = other.get_newest_item()

    if my_newest_item == None or their_newest_item == None:
        return False 
    else: 
        self.swap_items(other, their_newest_item, my_newest_item)
        return True 
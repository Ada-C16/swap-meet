class Vendor:
    def __init__(self, inventory= None):
        if not inventory:
            inventory = []
        self.inventory = inventory
        
    def add(self,item):
        self.inventory.append(item)
        return item
        
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    def get_by_category(self,category_name):
        item_list = []
        for item in self.inventory:
            if item.category == category_name:
                item_list.append(item)
        return item_list
    
    def swap_items(self,friend,my_item,their_item ):
        if my_item not in self.inventory  or their_item not in friend.inventory:
            return False
        self.remove(my_item)
        friend.add(my_item)
        friend.remove(their_item)
        self.add(their_item)
        return True
        
    def swap_first_item(self,friend):
        if self.inventory == [] or friend.inventory == []:
            return False
        first_item_self = self.inventory[0]
        first_item_friend = friend.inventory[0]
        self.swap_items(friend,first_item_self,first_item_friend)
        return True
    
    def get_best_by_category(self, category_name):
        best_condition = 0
        best_item = None
        for item in self.get_by_category(category_name):
            
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item
    
    def swap_best_by_category(self,other,my_priority,their_priority):
            
        my_priority = other.get_best_by_category(my_priority) 
        their_priority = self.get_best_by_category(their_priority)
        self.swap_items(other,their_priority,my_priority)
        if my_priority == None or their_priority == None:
            return False
        return True
        
    def get_new_item(self):
        newest_item = None
        first_item = self.inventory[0]
        min_age = first_item.age
        for item in self.inventory:
            if item.age < min_age:
                min_age = item.age
                newest_item = item
        return newest_item 
    
    def swap_by_newest(self, friend, my_newest_item, friend_newest_item):
        my_newest_item = self.get_new_item()
        friend_newest_item = friend.get_new_item()
        self.swap_items(friend, my_newest_item,friend_newest_item)
        if my_newest_item == None or friend_newest_item == None:
            return False
        return True

from swap_meet.item import Item
class Vendor(Item):
    pass
    def __init__ (self, inventory = []):
        self.inventory = inventory 
        
    def add(self, item):
        self.inventory.append(item)
        return item
        
    def remove(self, item):
        if item in  self.inventory:
           self.inventory.remove(item)
           return item
        if item not in self.inventory:
            return False

    def get_by_category(self, category):
        list_category = []
        items = self.inventory
        self.category = Item()
        for item in items:
            if item.category == category:
                list_category.append(item)
        return list_category

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.inventory.append(my_item)
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            return True 
        elif my_item not in self.inventory or their_item not in friend.inventory:
            return False 

    def swap_first_item(self,friend):
        if len(self.inventory) and len(friend.inventory) == 0:
            return False 
        elif len(self.inventory) and len(friend.inventory) > 0:
            item = self.inventory[0]
            friend_item = friend.inventory[0]
            self.swap_items(friend, item, friend_item)
            return True

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        highest_condition = 0
        best_condition_item = ""
        if len(category_list) == 0:
                best_condition_item = None
        for item in category_list:
            if item.condition > highest_condition:
                highest_condition = item.condition
                best_condition_item = item
        return best_condition_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):

        best_item_my_priority = other.get_best_by_category(my_priority)
        best_item_their_priority = self.get_best_by_category(their_priority)

        if len(self.get_by_category(their_priority)) and len(other.get_by_category(my_priority)) > 0:
            self.swap_items(other, best_item_their_priority, best_item_my_priority)
            return True
        
        


        
        
      
            
                
       
           
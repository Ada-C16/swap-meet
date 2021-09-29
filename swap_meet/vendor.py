class Vendor:
    def __init__(self, inventory = list()):
        if not inventory:
            inventory = []
        self.inventory = inventory
   
    # def __init__(self):
        
    #     self.inventory = []

    # def __init__(self, inventory = []):
    #     # if not inventory:
    #     #     inventory = []
    #     self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        item_list = [] 
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        
        return item_list

    def swap_items(self, friend_inv, this_item, their_item):
        if not this_item in self.inventory or not their_item in friend_inv.inventory:
            return False

        self.inventory.remove(this_item)
        friend_inv.inventory.append(this_item)
        friend_inv.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True

    def swap_first_item(self, friend_inv):
        if not self.inventory or not friend_inv.inventory:
            return False
        removed_self = self.remove(self.inventory[0])
        removed_friend = friend_inv.remove(friend_inv.inventory[0])
        self.add(removed_friend)
        friend_inv.add(removed_self)
        return True
    def get_best_by_category(self, category):
       best_item = None
       best_condition = 0.0
       match_list = []
       for item in self.inventory:
             match_list.append(item.category)

       if not category in match_list:
           return None 
                    
       for item in self.inventory:
             if item.category == category:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item
       return best_item
       
       

  

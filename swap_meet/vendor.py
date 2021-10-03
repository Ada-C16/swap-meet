from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory 
        self.item = Item()
    
    def add(self,item):
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        if item in self.inventory: 
            self.inventory.remove(item)
            return item
        else: 
            return False 

    def get_by_category(self, category):
        items = [] 
        for item in self.inventory: 
            if item.category == category: 
                items.append(item)
        return items 
# wave 3  
    def swap_items(self, friend, my_item, their_item):

        if my_item not in self.inventory or their_item not in friend.inventory: 
            return False
        #else:
        self.inventory.remove(my_item)  
        friend.inventory.append(my_item) 
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)  
        return True 
           

# wave 4 
    def swap_first_item(self,friend):

        if len(self.inventory) != 0 and len(friend.inventory) !=  0: 
            my_first_item = self.inventory[0]
            friend_first_item = friend.inventory[0]
            self.inventory.remove(my_first_item) 
            friend.inventory.append(my_first_item) 
            friend.inventory.remove(friend_first_item)
            self.inventory.append(friend_first_item) 
            return True
        else: 
            return False 


# wave 5 
    def condition_description(self,item):
     
        pass 


# wave 6  
    def get_best_by_category(): 
        pass 

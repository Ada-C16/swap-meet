#Wave 1
# from item import Item
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory
    def add(self,item):
        self.inventory.append(item)
        return item 
    def remove(self,item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item 
    
#Wave 2

    def get_by_category(self,category):
        items = []
        for item in self.inventory:
            if category == item.category:
                items.append(item)
        return items

#Wave 3 
    def swap_items (self,friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        else:
            friend.inventory.remove(their_item)
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            friend.inventory.append(my_item)
            
        return True 

#Wave4 
    def swap_first_item (self,friend): #friend is another Vender 
        if len(self.inventory) == 0 or len(friend.inventory) == 0 :
            return False
        
        self.inventory.append(friend.inventory[0])
        friend.inventory.append(self.inventory[0])
        self.inventory.pop(0)
        friend.inventory.pop(0)

    
        
        
        return True 
        


#Wave 5 

#look under item tab for the code 




#wave6

    def get_best_by_category(self, category):
        highest_condition = 0
        best_item = None
        
        for item in self.inventory:
            if item.condition > highest_condition and category == item.category: 
                highest_condition = item.condition
                best_item = item
        return best_item  
    
    def swap_best_by_category(self,other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)


        if their_best_item == None or my_best_item == None:
            return False
        
        
        else:
            self.swap_items(other, my_best_item, their_best_item)
            return True



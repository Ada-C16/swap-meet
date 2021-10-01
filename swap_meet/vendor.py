from swap_meet.item import Item
class Vendor:
    def __init__ (self,inventory= None ):
        self.inventory = inventory if inventory is not None else []

    def add(self, inventory_item):
        self.inventory.append(inventory_item)
        return inventory_item

    def remove(self, inventory_item):
        if inventory_item in self.inventory:
            self.inventory.remove(inventory_item)
            return inventory_item
        else:
            return False

    def get_by_category(self,category):
        items= []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self,other_vendor,my_item,their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
           other_vendor.add(my_item)
           self.remove(my_item)
           self.add(their_item)
           other_vendor.remove(their_item)
           return True
        else:
           return False
       
    def swap_first_item(self,other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            self.swap_items(other_vendor,self.inventory[0], other_vendor.inventory[0])
            return True
        
    def get_best_by_category(self,str_category):
        best_item = None
        rating_of_best_item = 0
        for item in self.inventory:
            if item.category == str_category and item.condition >= rating_of_best_item:
                best_item = item 
                rating_of_best_item = item.condition
        return best_item
    def swap_best_by_category(self,other,my_priority,their_priority):
        best_item_for_them = self.get_best_by_category(their_priority)
        best_item_for_me = other.get_best_by_category(my_priority)
        
        
        if best_item_for_me == None:
            return False
        elif best_item_for_them == None:
            return False
        else:
            self.swap_items(other,best_item_for_them,best_item_for_me)
        return True    
            
            
        
        
        
        
           
           



class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory
 

    def add(self, item):

        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    
    def get_by_category(self, category):

        return [item for item in self.inventory if item.category == category]
        
    def swap_items(self, other_vendor, this_item, their_item):

        if not this_item in self.inventory or not their_item in other_vendor.inventory:
            return False
       
        other_vendor.add(self.remove(this_item))
        self.add(other_vendor.remove(their_item))
        return True

    def swap_first_item(self, friend_inv):

        return False if not self.inventory or not friend_inv.inventory \
            else self.swap_items(friend_inv, self.inventory[0], friend_inv.inventory[0])
          

    def get_best_by_category(self, category):
        return max(self.get_by_category(category), key = lambda item: item.condition, default= None )

    def swap_best_by_category(self, other, my_priority, their_priority):

        my_best_to_swap = self.get_best_by_category(their_priority)
        their_best_to_swap = other.get_best_by_category(my_priority)
        
        return self.swap_items(other, my_best_to_swap, their_best_to_swap) if \
            my_best_to_swap and my_best_to_swap else False
    
        

       
       

  

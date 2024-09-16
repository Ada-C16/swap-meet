##WAVE 1##

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
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, items):
        return [item for item in self.inventory if item.category == items]

    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory and their_item in other.inventory:
            self.remove(my_item)
            other.remove(their_item)
            self.add(their_item)
            other.add(my_item)
            return True
        else:
            return False

    def swap_first_item(self, other):
        return self.swap_items(other, self.inventory[0], other.inventory[0])  if self.inventory and other.inventory else False
       
 ## Wave 6 ##
    def get_best_by_category (self, category):
        best_item = None
        best_condition = 0

        for item in self.inventory:

            if item.category == category:
                if item.condition > best_condition:
            
                    best_condition = item.condition
                    best_item = item

        return best_item
        ### This part could use refactoring. but... 
   
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_item, their_item)  


  ## enhancements-- swap_by_newewst ###   




    



from typing import ItemsView


class Vendor():
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
    
    
    def add(self, item):
        self.inventory.append(item)
        return item    
    
    def remove(self, item):
        if item not in self.inventory:
            return None
        else:
            self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items_of_same_category = []

        for item in self.inventory:
            if item.category == category:
                items_of_same_category.append(item)

        return items_of_same_category

    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend_vendor.inventory:
            return False
        self.remove(my_item)
        friend_vendor.add(my_item)
        friend_vendor.remove(their_item)
        self.add(their_item)

        return True
    def swap_first_item(self, friend_vendor):
        if self.inventory == [] or friend_vendor.inventory == []:
            return False
        return self.swap_items(friend_vendor, self.inventory[0], friend_vendor.inventory[0])

    def get_best_by_category(self, category):
        best_item = None
        for item in self.inventory:
            if item.category == category:
                if best_item == None:
                    best_item = item
                else:
                    if best_item.condition < item.condition:
                        best_item = item

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_choice = other.get_best_by_category(my_priority)
        their_choice = self.get_best_by_category(their_priority)
        return self.swap_items(other, their_choice, my_choice)
    


        

            
        


        


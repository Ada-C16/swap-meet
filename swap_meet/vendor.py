from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, string_category):
        list_of_items = []
        for i in range(len(self.inventory)):
          if string_category == self.inventory[i].category:
                list_of_items.append(self.inventory[i])       
        return list_of_items

    def swap_items(self, friends_inventory, my_item, their_item):
        if my_item in self.inventory and their_item in friends_inventory.inventory:
            self.add(their_item)
            friends_inventory.add(my_item)
            self.remove(my_item)
            friends_inventory.remove(their_item)
            return True
        else:
            return False
                 
    def swap_first_item(self, friends_inventory):
        if self.inventory and friends_inventory.inventory:
            temp_first_item = self.inventory[0]
            friends_first_item = friends_inventory.inventory[0]
            self.remove(self.inventory[0])
            friends_inventory.remove(friends_inventory.inventory[0])
            friends_inventory.add(temp_first_item)
            self.add(friends_first_item)
            return True
        else:
            return False

    def get_best_by_category(self, category):
        if not self.get_by_category(category):
            return None

        best_condition = 0
        item_with_best_condition = 0

        for item in self.get_by_category(category):
            if item.condition > best_condition:
                best_condition = item.condition
                item_with_best_condition = item

        return item_with_best_condition
            

    
     
        

      


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

    # def get_by_category(self, string_category):
    #     list_of_items = []
    #     for i in range(len(self.inventory)):
    #         if self.inventory[i] == string_category:

    #             list_of_items.append(Item(self.inventory[i]))
                
    #     return list_of_items

    def swap_items(self, friends_inventory, my_item, their_item):
        if my_item in self.inventory and their_item in friends_inventory.inventory:
            self.add(their_item)
            friends_inventory.add(my_item)
            self.remove(my_item)
            friends_inventory.remove(their_item)
            return True
        else:
            return False
            
          
      


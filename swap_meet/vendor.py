#Wave 1
# from item import Item
class Vendor:
    def __init__(self, inventory=[]):
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






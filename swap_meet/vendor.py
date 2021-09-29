class Vendor:
    def __init__(self, inventory= None):
        if not inventory:
            inventory = []
        self.inventory = inventory
        
    def add(self,item):
        self.inventory.append(item)
        return item
        
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    def get_by_category(self,catagory_name):
        mylist = []
        for item in self.inventory:
            if item.category == catagory_name:
                mylist.append(item)
        return mylist
    
    def swap_items(self,friend,my_item,their_item ):
        if my_item not in self.inventory  or their_item not in friend.inventory:
            return False
        self.remove(my_item)
        friend.add(my_item)
        friend.remove(their_item)
        self.add(their_item)
        return True
        
    def swap_first_item(self,friend):
        if self.inventory == [] or friend.inventory ==[]:
            return False 
        first_item_self = self.inventory[0]
        first_item_friend = friend.inventory[0]
        self.remove(first_item_self)
        self.add(first_item_friend)
        friend.remove(first_item_friend)
        friend.add(first_item_self)
        return True
    def get_best_by_category(self, category_name):
         pass

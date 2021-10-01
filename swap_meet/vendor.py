from swap_meet.item import Item #why here??

class Vendor:
    def __init__(self, inventory= None):
        if not inventory:   # if inventory is None: 
            inventory = []
        self.inventory = inventory

    
    def add(self, item):
        """
        This method adds the item to our inventory.
        """
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        """
        This method will remove a matching item in our inventory.
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category): 
        items = []
        #self.category = category
        for item in self.inventory:             #item here is an instance of the class Item 
            if item.category == category:  #what???
                items.append(item)  
        return items

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        self.remove(my_item)
        friend.add(my_item)  
        friend.remove(their_item)
        self.add(their_item)
        return True 

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False

        first_item = self.inventory[0]
        first_other_item = friend.inventory[0]

        self.inventory.append(first_other_item)
        friend.inventory.append(first_item)
        friend.inventory.remove(first_other_item)
        self.inventory.remove(first_item)
        return True

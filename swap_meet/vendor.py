class Vendor:
    def __init__(self, inventory= None):
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
        return False  

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if  item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, friend_vendor, my_item, friend_item) :
        if my_item not in self.inventory or friend_item not in friend_vendor.inventory:
            return False
        elif my_item not in friend_vendor.inventory and friend_item not in self.inventory:
            friend_vendor.add(my_item)
            self.remove(my_item)
            self.add(friend_item)
            friend_vendor.remove(friend_item)
            return True
        return False
        
        
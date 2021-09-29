from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        # self.item = Item()
        if not inventory:
            inventory=[]
        self.inventory=inventory 
        


    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        
        if item not in self.inventory:
            return False
            
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        
        category_list=[] 
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list
    
    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.append(their_item)
            vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            vendor.inventory.remove(their_item)
            return True

        return False



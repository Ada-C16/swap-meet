from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
            
        self.inventory = inventory 

    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item

    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False 
        #from here up passes wave 1

### WAVE 2 ###
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category
    
### Wave 3 ###
    def swap_items(self, vendor, my_item, their_item):
    
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
    
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        self.add(their_item)
        return True
    
### WAVE 4 ###
    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        self.swap_items(vendor,self.inventory[0], vendor.inventory[0])
        return True
    
### WAVE 6 ###
    def get_best_by_category(self,category):
        max_condition = 0
        quality_item = ""
        category_list = self.get_by_category(category)
        if len(category_list) == 0:
            return None

        for item in category_list:
            if item.condition > max_condition:
                max_condition = item.condition
                quality_item = item
        return quality_item
    
    def swap_best_by_category(self,other, my_priority,their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if my_best_item and their_best_item:
            self.swap_items(other,my_best_item,their_best_item)
            return True
        return False

    def get_newest_item(self):
        newest_item = self.inventory[0]
        min_age = self.inventory[0].age
        for index in range(len(self.inventory)):
            if self.inventory[index].age <  min_age:
                min_age = self.inventory[index].age
                newest_item = self.inventory[index]
        return newest_item
    def swap_by_newest(self, other):
        others_newest_item = other.get_newest_item()
        result = self.swap_items(other, self.get_newest_item(), others_newest_item)
        return result

class Vendor:
    def __init__(self, inventory=None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
            

    def add(self, add_new_item):
        self.inventory.append(add_new_item)
        return (add_new_item)

    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return (remove_item)
        else:
            return False

    def get_by_category(self, category_name):
        item_list = []
        for inventory in self.inventory:
            if inventory.category == category_name:
                item_list.append(inventory)
        return item_list

    def swap_items(self, vendor, my_item, their_item):
        if my_item  in self.inventory and their_item in vendor.inventory:
            self.inventory.append(their_item)
            vendor.inventory.remove(their_item)
            vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            return True
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

    def swap_first_item(self, another_vendor):
        if len(self.inventory) and len(another_vendor.inventory) == 0:
            return False
        elif len(self.inventory) and len(another_vendor.inventory) > 0:
            my_item = self.inventory[0]
            their_item = another_vendor.inventory[0]
            self.swap_items(another_vendor,my_item,their_item)
            return True

    def get_best_by_category(self,category):
        category_items = self.get_by_category(category)
        counter = 0 
        best_item = ''
        if len(category_items) == 0:
                best_item = None
        for item in category_items:
            
            if item.condition > counter:
                counter = item.condition
                best_item = item 
        return best_item
                
    def swap_best_by_category(self,other,my_priority,their_priority):
        what_i_want = other.get_best_by_category(my_priority)
        what_they_want = self.get_best_by_category(their_priority)
        if len(self.get_by_category(their_priority)) and len(other.get_by_category(my_priority)) == 0:
            return False
        elif len(self.get_by_category(their_priority)) and len(other.get_by_category(my_priority)) > 0:
            self.swap_items(other,what_they_want, what_i_want)
            return True










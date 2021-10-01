class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, vendor, my_item, their_item):
        if their_item not in vendor.inventory or my_item not in self.inventory:
            return False
        else:
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            return True

    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        else:
            my_new_item = vendor.inventory[0]
            their_new_item = self.inventory[0]
            self.swap_items(vendor, their_new_item, my_new_item)
            return True

    def get_best_by_category(self, category):
        best_quality = 0
        try:
            for item in self.inventory:
                if item.category == category:
                    if item.condition > best_quality:
                        best_quality = item.condition
                        best_item = item
            else:
                return best_item 
        except UnboundLocalError as err:
            return None

                
    def swap_best_by_category(self, other, my_priority, their_priority):
        their_new_item = self.get_best_by_category(their_priority)
        my_new_item = other.get_best_by_category(my_priority)
        if their_new_item == None or my_new_item == None:
            return False
        else:
            self.swap_items(other, their_new_item, my_new_item)
            return True

    def get_by_newest(self, other):
        my_item_age = 10000
        for item in self.inventory:
            if item.age < my_item_age:
                my_item_age = item.age
                my_newest_item = item
        
        their_item_age = 10000
        for item in self.inventory:
            if item.age < their_item_age:
                their_item_age = item.age
                their_newest_item = item
        
        if their_newest_item == None or my_newest_item == None:
            return False
        else:
            self.swap_items(other, my_newest_item, their_newest_item)
            return True
from .item import Item
class Vendor:
    def __init__(self, inventory=[]):
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
    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == Item(category=category).category]
    
    def swap_items(self, Vendor, my_item, their_item):
        
        if my_item in self.inventory and their_item in Vendor.inventory:
            Vendor.remove(their_item)
            self.add(their_item)
            Vendor.add(my_item)
            self.remove(my_item)
            return True
        else:
            print("over here")
            return False
    def swap_first_item(self, Vendor):
        if len(self.inventory) > 0 and len(Vendor.inventory) > 0:
            self.swap_items(Vendor, self.inventory[0], Vendor.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self, category):
        # for item in self.inventory:
        #     if item in self.get_by_category(category=category)\
        #         and
        record = [0,None]
        for item in self.inventory:
            if item in self.get_by_category(category):
                if item.condition > record[0]:
                    record[0] = item.condition
                    record[1] = item

        return record[1]
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_offer = self.get_best_by_category(their_priority)
        their_offer = other.get_best_by_category(my_priority)
        self.swap_items(other, my_offer, their_offer)
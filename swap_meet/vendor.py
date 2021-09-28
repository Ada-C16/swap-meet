class Vendor:
    def __init__(self, inventory=[]):
        self.inventory=inventory
    def add(self, item): 
        self.inventory.append(item)
        return item
    def remove(self, item): 
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    def get_by_category(self,category):
        cat_list=[]
        for item in self.inventory:
            if item.category==category:
                cat_list.append(item)
        return cat_list
    def swap_items(self, Vendor, my_item, their_item):
        if my_item in self.inventory and their_item in Vendor.inventory:
            self.remove(my_item)
            Vendor.add(my_item)
            Vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False

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
    def swap_first_item(self, Vendor):
        
        if self.inventory==[] or Vendor.inventory==[]:
            return False
        else:
            self_first_item=self.inventory[0]
            Vendor_first_item=Vendor.inventory[0]
            self.remove(self_first_item)
            Vendor.add(self_first_item)
            Vendor.remove(Vendor_first_item)
            self.add(Vendor_first_item)
            return True
    def get_best_by_category(self, category):
        cat=self.get_by_category(category)
        cond_list=[]
        if not cat:
            return None
        else:
            for item in cat:
                cond_list.append(item.condition)
            if item.condition==max(cond_list):
                return item
                
    def swap_best_by_category(self,other,my_priority,their_priority):
        #which will swap the best item of certain categories with another Vendor
        #The best item in my inventory that matches their_priority category is swapped with the best item in other's inventory that matches my_priority
            return True
           # If the Vendor has no item that matches their_priority category, swapping does not happen, and it returns False
           # If other has no item that matches my_priority category, swapping does not happen, and it returns False





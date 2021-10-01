from .item import Item 
class Vendor:
    #Wave 01
    def __init__(self,inventory=None): 
        self.inventory = inventory if inventory is not None else []
    
    def add(self,item):
        '''
        input: one item
        - adds item to the inventory
        output: item added 
        '''
        self.inventory.append(item)
        return item
    def remove(self,item):
        '''
        input: one item
        - removes item from inventory if there is a mathcing item 
        output: item removed , False if no matching item 
        '''
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False 
    #Wave 02
    def get_by_category(self,category):
        '''
        input: a string representing a category
        output: a list of items in the inventory(list) with that category
        '''
        result_list = []
        for item in self.inventory:
            if category == item.category:
                result_list.append(item)
        return result_list
        
        # return new list that is a sub-set of inventory list.
        
    


    #Wave 03
    def swap_items(self,other_vendor, my_item,their_item):
        '''
        input: other vendor(friend vendor is swappign with),
        instance of Item (vendor plans to give), 
        instance of Item (other vendor plans to give)
        - removes my_item from this Vendor's inventory and adds 
        it to friends/other vendor inventory
        - removes their_item from friend/other Vendor inventory and adds
        to this Vendors inventory 
        output: True if items are in inventories , False if either item is
        not in others inventory. 
        '''
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            self.add(their_item) 
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
        else:
            return False
            


        

    #Wave 04
    def swap_first_item(self,freind_vend):
        pass

    #Wave 06
    def get_best_by_category(self,category):
        pass
    def swap_best_by_category(self,other_vendor, my_priority,their_priority):
        pass


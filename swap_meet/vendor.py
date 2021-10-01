from .item import Item 
class Vendor:
    #Wave 01
    def __init__(self,inventory=None): 
        self.inventory = inventory if inventory is not None else []
    
    def add(self,item):
        '''
        input: one item
        - adds item to the inventory
        output: returns item added 
        '''
        self.inventory.append(item)
        return item
    def remove(self,item):
        '''
        input: one item
        - if there is a mathcing item, removes item from inventory  
        output: returns item removed if item is valid(matching item) 
                else: returns False
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
        output: returns list of items in the 
        inventory(list) with that category
        '''
        result_list = []
        for item in self.inventory:
            if category == item.category:
                result_list.append(item)
        return result_list
        
        

    #Wave 03
    def swap_items(self,other_vendor, my_item,their_item):
        '''
        input: instance of (other) Vendor,
            instance of Item (this vendor plans to give), 
            instance of Item (other vendor plans to give)
        - if both items present in correspeonding Vendor inventory list
            removes item from corresponding inventory list and adds to 
            inventory list of oppisite vendor.
        output: returns True: if items in list and swapped
                else: returns False
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
    def swap_first_item(self,other_vendor):
        '''
        input: instance of (other) Vendor
        - if both list are valid (not empty), switches first item of 
            each other vendors and this vendor 
            inventory list with each other. 
        output: returns False: if either inventory empty
                else: returns True 
        '''
        if  bool(self.inventory) == False or  bool(other_vendor.inventory) == False:
            return False
        else: 
            my_first_item = self.inventory.pop(0)
            their_first_item = other_vendor.inventory.pop(0)
            self.inventory.insert(0, their_first_item)
            other_vendor.inventory.insert(0, my_first_item)
            return True

    #Wave 06
    def get_best_by_category(self,category):
        '''
        input: a string that represents a category
        - looks through inventory for item with matching category 
            and best(highest value) condition. 
        output: returns item: if there is a valid item (matching condition)
                else: returns None
        * returns sinlge item only, even if there
                are same items with same condition in inventory.
        '''
        matching_category_list = self.get_by_category(category)
        best_condition_num = 0
        best_condition_item = None
        if matching_category_list:
            for item in matching_category_list:
                if item.condition > best_condition_num:
                    best_condition_num = item.condition
                    best_condition_item = item
            return best_condition_item
        else: 
            return None


    def swap_best_by_category(self,other = "", my_priority= "",their_priority=""):
        '''
        input: instance of other Vendor, 
            my_priority(category this vendor wants)
            thier_priority(category other vendor wants to receive)
        - if both vendors have item in inventory that match category of 
            opposing vendor priority category: best items(greatest condition) 
            that matches each vendors priority is swapped 
            from invetory to oppossing vendors inventory
        output : returns True : if matches found and items swapped
                else: returns False 
        '''
        result = None
        my_best_item = self.get_best_by_category(their_priority)  
        their_best_item = other.get_best_by_category(my_priority)
        result = self.swap_items(other, my_best_item,their_best_item)
        return result



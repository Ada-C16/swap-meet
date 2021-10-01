class Vendor():
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

    def get_by_category(self, category_string):
        list_by_category =[]
        for item in self.inventory:
            if item.category == category_string:
                list_by_category.append(item)
        return list_by_category

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if len(self.inventory)> 1 and len(vendor.inventory)> 1:
        # storing first item of self.inventory and vendor. inventory in 2 variables
            my_first_item = self.inventory[0]
            their_first_item = vendor.inventory[0]
        # removing and adding items using variables
            self.inventory.remove(my_first_item)
            self.inventory.append(their_first_item)
            vendor.inventory.remove(their_first_item)
            vendor.inventory.append(my_first_item)
            return True
        else:
            return False
    def get_best_by_category(self, category):
    # using get_by_category method, storing result in new variable, items_by_category
    # items_by_category is now a list of objects that meet the category criteria
        items_by_category = self.get_by_category(category)
        if len(items_by_category)== 0:
            return None
        else:
    #using list comprehension to compare just the condition attributes of the items objects
    #in items_by_category list.  looking for the max value of these attributes
    #storing the max value, a float, in the max_condition variable
            max_condition =max(item.condition for item in items_by_category)
    #now going through items_by_category looking for which item's condition attribute
    #matches max_condition and returning that whole item
            for item in items_by_category:
                if item.condition == max_condition:
                    return item

    def swap_best_by_category(self, other, my_priority, their_priority):
    #using the get_best_by_category method twice, once for Vendor (self) and once for
    #Vendor(other).  Store the results of those method calls in 2 separate variables    
        my_best = self.get_best_by_category(their_priority)
        their_best =other.get_best_by_category(my_priority)
        if my_best == None or their_best == None:
            return False
    #call the swap_items method, using the 2 variables my_best, their_best
    #as arguments
        else:
            self.swap_items(other, my_best, their_best)
            return True
    def swap_by_newest(self, other):
    #using list comprehension to compare only the age attributes of all the item objects 
    #in inventory and return the lowest value (for newest item). do this twice for self.inventory
    #and other.inventory. Frankly, I'm amazed this works. Store results in 2 variables
        my_newest = min(item.age for item in self.inventory)
        their_newest = min(item.age for item in other.inventory)
        if my_newest == None or their_newest == None:
            return False
    #call the swap_items method using 2 variables, my_newest, their newest
        else:
            self.swap_items(other, my_newest, their_newest)
            return True








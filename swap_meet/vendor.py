from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None, category=Item):
       
        if not inventory:
            inventory=[]
        self.inventory=inventory
        self.category=category
        
#With this method I am feeding the list of inventory with the items passed in the parameter and now item
#  is a component of vendor   
    def add(self, item):
        self.inventory.append(item)
        return item
    
#With this method I am taking out of the list of inventory with the items passed in the parameter 
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

# I am creating a list of items that share the same category attribute
    def get_by_category(self, category):
        category_list=[]
        for item in self.inventory:
            if item.category==category:
                category_list.append(item)
        return category_list

#With this method, if me, and the second instance have items to trade in our inventory lists...
# I am removing from my inventory list the item(object) passed in the parameter which
# is the one that I will give away and putting it in the other instance's inventory, at the same time
# I am adding to my list of inventory the item the other instance is traiding  and getting out of its inventory list.
# For this I am calling the two previous methods I've created passing my_item and their item as parameters. 
    def swap_items(self, vendor, my_item, their_item):
    
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            vendor.add(my_item)
            self.add(their_item)
            vendor.remove(their_item)
            return True
        return False

 #First, I am checking that my list of inventory or the second instance's list of inventory have at least one object
 # in order to be eable to swap, once this condition is True, I called the swap.items method, passing as parameters
 #the first object on the inventory lists, by setting the index to 0 on each list.
    def swap_first_item(self, vendor):
        if len(self.inventory)<1 or len(vendor.inventory)<1:
            return False
        self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        return True

#This method gets the best item by category for this, I defined a variable to 
# store the maximum value of the condition attribute, the I looped through the list of objects that share the same category
# in this case the category given in the parameter. I set the variable to 0 so every time the loop runs if the attribute
# condition in each object is greater than the one before it will replace it and it will be the new highest and will return
# the item.       
    def get_best_by_category(self, given_category):
     
        best_condition=0
        best_item=None
    
        for item in self.get_by_category(given_category):
            if item.condition>best_condition:
                best_condition=item.condition
                best_item=item
              
        return best_item
            
#With this method I am getting the items to swap, by calling the method of best by category, once I have the desired items
# by self and the second instance each into a variable, now I call my swap_item method passing these variables as the parameters
# In case these variables (parameters) don't contain a value, the swap method will return False. 
    def swap_best_by_category(self,other,my_priority, their_priority):
        my_best_item=self.get_best_by_category(their_priority)
        their_best_item=other.get_best_by_category(my_priority)
        if not my_best_item or not their_best_item:
            return False
        
        self.swap_items(other,my_best_item,their_best_item)
        return True

    


    
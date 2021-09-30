class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except: 
            return False

    def get_by_category(self, type):
        '''
        returns a list of Items in the inventory with the same category as 'type'
        '''
        item_list = []
        for item in self.inventory:
            if type == item.category:
                item_list.append(item)
        return item_list

    def swap_items(self, vendor, my_item, their_item):

        if my_item in self.inventory and their_item in vendor.inventory:
            vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            vendor.inventory.remove(their_item)
            return True
        else: 
            return False

    def swap_first_item(self, vendor):

        vendor_inventory = vendor.inventory.copy()
        self_inventory = self.inventory.copy()

        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        else:
            first_item_a = self_inventory[0]
            first_item_b = vendor_inventory[0]
            self.inventory[0] = first_item_b
            vendor.inventory[0] = first_item_a
            return True

    def get_best_by_category(self, type):
    
        item_list = self.get_by_category(type)
        highest_condition = 0
        
        if len(item_list) == 0:
            return None
        else:
            for item in item_list:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    highest_item = item

            return highest_item

    def swap_best_by_category(self, other, my_priority, their_priority):

        vendor_best_item = self.get_best_by_category(their_priority)
        other_best_item = other.get_best_by_category(my_priority)

        if vendor_best_item == None or other_best_item == None:
            return False
        else:
            self.inventory.append(other_best_item)
            other.inventory.append(vendor_best_item)
            self.inventory.remove(vendor_best_item)
            other.inventory.remove(other_best_item)
            return True

                    

       

       

            
        


        
            



        


    
    
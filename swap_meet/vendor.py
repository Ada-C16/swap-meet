# Wave 1

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

        
            



        


    
    
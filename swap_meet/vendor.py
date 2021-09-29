from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory: 
            inventory = []
        self.inventory = inventory # List of item objects

    def add(self, item):
        """
        Adding item to inventory. 
        """
        self.inventory.append(item)
        return item
    
    def remove(self, item): 
        """
        Removing item from inventory. 
        Returning false if not in inventory.
        """
        if item not in self.inventory:
            return False 
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        """
        Returning items within a given category
        """
        category_items_list = []

        for item in self.inventory: 
            if item.category == category:
                category_items_list.append(item)
        
        return category_items_list

    def swap_items(self, other_vendor, my_item, their_item):
        """
        Swapping items between two vendors. 
        Returns false if items not in one or both inventories. 
        """
        # Returning false if items not in one or both inventories. 
        if my_item not in self.inventory or \
        their_item not in other_vendor.inventory: 
            return False

        # Swapping my_item
        self.remove(my_item)
        other_vendor.add(my_item)

        # Swapping their_item
        self.add(their_item)
        other_vendor.remove(their_item)

        return True

    def swap_first_item(self, other_vendor):
        """
        Swapping first item in vendors' inventories. 
        Returns false if either inventory is empty. 
        """
        # Returning false if either inventory is empty. 
        if len(self.inventory) == 0 or \
        len(other_vendor.inventory) == 0:
            return False

        # Initializing variables to represent first item in vendors' inventories.
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        # Calling swap_items with first item in inventory variables set. 
        result = self.swap_items(other_vendor, my_first_item, their_first_item)
        
        return result

    def get_best_by_category(self, category): 
        """
        Returns item with highest condition score within a category.
        """
        # Initializing variables
        items_in_category = self.get_by_category(category)
        highest_condition = 0.0
        best_item = ""

        # Returning None if there are no items in the category
        if not items_in_category: 
            return None 

        # Identifying item with highest condition rating.
        for item in items_in_category:
            if item.condition > highest_condition:
                highest_condition = item.condition
                best_item =item

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """"""

from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        inventory = [] if not inventory else inventory
        self.inventory = inventory

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
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other_vendor, my_item, their_item):
        """
        Swapping items between two vendors. 
        Returns false if items not in one or both inventories. 
        """
        if my_item not in self.inventory or \
        their_item not in other_vendor.inventory:                   # How to use ternary operator here?
            return False

        self.remove(my_item)
        other_vendor.add(my_item)

        self.add(their_item)
        other_vendor.remove(their_item)

        return True

    def swap_first_item(self, other_vendor):
        """
        Swapping first item in vendors' inventories. 
        Returns false if either inventory is empty. 
        """
        if len(self.inventory) == 0 or \
        len(other_vendor.inventory) == 0:
            return False

        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        result = self.swap_items(other_vendor, my_first_item, their_first_item)
        
        return result

    def get_best_by_category(self, category): 
        """
        Returns item with highest condition score within a category.
        """
        items_in_category = self.get_by_category(category)
        highest_condition = 0.0
        best_item = ""

        if not items_in_category: 
            return None 

        for item in items_in_category:
            if item.condition > highest_condition:
                highest_condition = item.condition
                best_item = item

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """
        Returns True if both vendors trade best conditioned item from preferred cateogry. 
        Returns False if either vendor doesn't have an item in the other's preferred cateogry. 
        """
        taken_item = other_vendor.get_best_by_category(my_priority)
        given_item = self.get_best_by_category(their_priority)

        if not taken_item or not given_item:
            return False 

        self.swap_items(other_vendor, given_item, taken_item)

        return True
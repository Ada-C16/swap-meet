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

    def swap_items(self, friend, my_item, their_item):
        """
        Swapping items between two vendors. 
        Returns false if items not in one or both inventories. 
        """
        if my_item not in self.inventory or \
        their_item not in friend.inventory: 
            return False

        # Swapping my_item
        self.inventory.remove(my_item)
        friend.inventory.append(my_item)

        # Swapping their_item
        self.inventory.append(their_item)
        friend.inventory.remove(their_item)

        return True


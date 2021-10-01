from swap_meet.item import Item 


class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory
        self.item = Item()


    def add(self, item):
        """
        Takes one parameter item, adds to 
        inventory, returns item
        """
        self.inventory.append(item)
        return item 


    def remove(self, item):
        """
        Takes one parameter item, removes from
        inventory, returns item
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        else:
            return False 


    def get_by_category(self, category):
        """
        Takes one parameter category,
        populates list items of a certain 
        category, returns items
        """
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items


    def swap_items(self, other, my_item, other_item):
        """
        Takes in three parameters other (vendor), my_item,
        other_item; returns Boolean based on whether swap 
        is possible: only if the items are in stock
        """
        if my_item not in self.inventory or other_item not in other.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            other.inventory.append(my_item)
            other.inventory.remove(other_item)
            self.inventory.append(other_item)
            return True 


    def swap_first_item(self, other):
        """
        Takes in 1 parameter other (vendor); returns 
        Boolean based on whether each vendor has inventory
        and swaps the first item in their inventory
        """
        if len(self.inventory) != 0 and len(other.inventory) != 0: 
            return self.swap_items(other, self.inventory[0], other.inventory[0])
        else:
            return False


    def get_best_by_category(self, category=""):
        """
        Takes one parameter category, which 
        default value is an empty str, returns 
        the best item rated by category
        """
        items_by_category = self.get_by_category(category)
        if len(items_by_category) == 0:
            return None
        
        return max(items_by_category, key=lambda item: item.condition)


    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Takes three parameters, other (vendor), and each vendor's
        priority item; returns a Boolean based on whether each 
        vendor has inventory to perform a swap
        """
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False

        best_item = self.get_best_by_category(category=their_priority)
        their_best_item = other.get_best_by_category(category=my_priority)

        return self.swap_items(other, best_item, their_best_item)
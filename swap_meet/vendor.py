class Vendor:
    
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        '''Takes in an item and appends it to self's list of inventory.'''
        
        self.inventory.append(item)

        return item

    def remove(self, item):
        '''Takes in an item and removes it from self's list of inventory.'''

        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return None

    def get_by_category(self, category):
        '''Takes in a category as a string and returns items with a matching category as a list.'''
        
        items_in_category = []

        for item in self.inventory:
            if item.category == category.title():
                items_in_category.append(item)

        return items_in_category

    def has_item(self, item):
        '''Takes in an item and returns a boolean if it is in self's inventory'''
        return item in self.inventory

    def swap_items(self, vendor2, item1, item2):
        '''
        Takes in another vendor, and item in self's inventory, and an item in the other vendor's inventory.
        Adds the first item to the other vendor's inventory and removes it from self's inventory.
        Adds the second item to self's inventory and removes it from the other vendor's inventory.
        Returns True if the swap was completed and False if it was note.
        '''
        
        if self.has_item(item1) and vendor2.has_item(item2):
            self.remove(item1)
            vendor2.add(item1)
            vendor2.remove(item2)
            self.add(item2)
            return True

        return False

    def swap_first_item(self, vendor2):
        '''
        Take in another vendor.
        Swap the first item in each vendor's inventory.
        Return True if the swap was completed successfully and False if not.
        These docstrings feel like they are just as long as the functions themselves, if not longer.
        '''
        if self.inventory and vendor2.inventory:
            first_item1 = self.inventory[0]
            first_item2 = vendor2.inventory[0]
            return self.swap_items(vendor2, first_item1, first_item2)

        return False

    def get_best_by_category(self, category):
        '''
        Take in a category.
        Return the item in that category with the highest condition rating.
        '''
        items_in_category = self.get_by_category(category)

        # lamda allows us to define a function inline for the key to decide which will determine how the items are compared
        best_item = max(items_in_category, key=lambda item: item.condition, default=None)

        return best_item

    # I'm not sure why these need keyword aruguments????
    def swap_best_by_category(self, other="", my_priority="", their_priority=""):
        '''
        Take in another vendory, a category self wants, ad a category the other vendor wants.
        Swap the best item in the preferred category between the two vendors.
        Return True if it was completed successfully and False if not. 
        '''
        
        my_best_item = self.get_best_by_category(their_priority)

        vendor2_best_item = other.get_best_by_category(my_priority)

        if not (my_best_item and vendor2_best_item):
            return False

        return self.swap_items(other, my_best_item, vendor2_best_item)

    def get_newest_item(self, category = ""):
        '''
        Optionally, take in a category.
        If no category specified, return the neweset item the vendor has in any category.
        Otherwise, return the newest item in the category.
        '''
        if not category:
            return min(self.inventory, key=lambda item: item.age, default=None)

        return min(self.get_by_category(category), key=lambda item: item.age, default=None)

    def swap_by_newest(self, vendor2, category1 ="", category2 = ""):
        '''
        Take in another vendor. Optionally, take in a category I want and a category the other vendor wants.
        Swap the newest item each vendor has.
        If a category is provided, swap the newest item in that category.
        Return True if the swap was completed successfully and False if it was not.
        '''
        my_newest_item = self.get_newest_item(category2)
        vendor2_newest_item = vendor2.get_newest_item(category1)

        if not (my_newest_item and vendor2_newest_item):
            return False

        return self.swap_items(vendor2, my_newest_item, vendor2_newest_item)

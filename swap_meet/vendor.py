class Vendor:
    
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        
        self.inventory.append(item)

        return item

    def remove(self, item):

        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return None

    def get_by_category(self, category):
        
        items_in_category = []

        for item in self.inventory:
            if item.category == category.title():
                items_in_category.append(item)

        return items_in_category

    def has_item(self, item):
        return item in self.inventory

    def swap_items(self, vendor2, item1, item2):
        
        if self.has_item(item1) and vendor2.has_item(item2):
            self.remove(item1)
            vendor2.add(item1)
            vendor2.remove(item2)
            self.add(item2)
            return True

        return False

    def swap_first_item(self, vendor2):
        if self.inventory and vendor2.inventory:
            first_item1 = self.inventory[0]
            first_item2 = vendor2.inventory[0]
            self.remove(first_item1)
            vendor2.add(first_item1)
            vendor2.remove(first_item2)
            self.add(first_item2)
            return True

        return False

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)

        # lamda allows us to define a function inline for the key to decide which will determine how the items are compared
        best_item = max(items_in_category, key=lambda item: item.condition, default=None)

        return best_item

    # I'm not sure why these need keyword aruguments????
    def swap_best_by_category(self, other="", my_priority="", their_priority=""):
        
        my_best_item = self.get_best_by_category(their_priority)

        vendor2_best_item = other.get_best_by_category(my_priority)

        if not (my_best_item and vendor2_best_item):
            return False

        return self.swap_items(other, my_best_item, vendor2_best_item)

    def get_newest_item_with_optional_category(self, category = ""):
        '''
        If no category specified, returns the neweset item the vendor has in any category.
        Otherwise, returns the newest item in the category.
        '''
        if not category:
            return min(self.inventory, key=lambda item: item.age, default=None)

        return min(self.get_by_category(category), key=lambda item: item.age, default=None)

    def swap_by_newest(self, vendor2, category1 ="", category2 = ""):
        '''
        Swap the newest item each vendor has. 
        Optionally, pass in a category to get the newest item in that category.
        '''
        my_newest_item = self.get_newest_item(category1)
        vendor2_newest_item = vendor2.get_newest_item(category2)

        if not (my_newest_item and vendor2_newest_item):
            return False

        return self.swap_items(vendor2, my_newest_item, vendor2_newest_item)

class Vendor:
    def __init__(self, inventory = []):
        """
        vendor class creates inits an empty list
        or takes inventory list
        """
        self.inventory = inventory

    def add(self, item):
        """
        adds item to inventory and returns item
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        removes item from inventory, returns false
        if item is not in inventory
        returns removed item.
        dint use .pop .index because of Time Com
        """
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item
        
    def get_by_category(self, category_name):
        """
        gets list of items that match category name
        returns empty list if category name is empty
        """
        category = []
        if category_name == "":
            return category

        category = [i for i in self.inventory if i.category.lower() == category_name.lower()]
        return category

    def swap_items(self, other_vendor, my_item, their_item):
        """
        takes 3 params other vendor, swaps my item into their inventory
        and theirs into mine returns false if neither is in their inventory
        """

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        their_swap = other_vendor.remove(their_item)
        my_swap = self.remove(my_item)

        return self.add(their_swap) and other_vendor.add(my_swap)


    def swap_first_item(self, other_vendor):
        """
        swaps first items in other vendor's inventory and mine
        """
        if self.inventory == [] or other_vendor.inventory == []:
            return False

        my_first_item = self.inventory[0]
        thier_first_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first_item, thier_first_item)
        

    def get_best_by_category(self, category):
        """
        gets item with best condition from category
        uses capitalize in case string is provided in lowercase 
        it ensure it matches category
        """
        
        category = category.capitalize()

        matching_category_from_inventory = self.get_by_category(category)

        best_condition = 0
        best_item = None

        for item in matching_category_from_inventory:
            if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item


        return best_item
        

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        other - the other vendor
        my_priority = the category vendor wants to receive
        their_priority = category other vendor wants to recive
        """
        if self.get_best_by_category(their_priority) == None or other.get_best_by_category(my_priority) == None:
            return False

        thier_priority_from_my_inv = self.get_best_by_category(their_priority)
        my_priority_from_their_inv = other.get_best_by_category(my_priority)
        

        return self.swap_items(other, thier_priority_from_my_inv, my_priority_from_their_inv)
    #def get_by_newest(self):
        
    #def swap_by_newest(self):

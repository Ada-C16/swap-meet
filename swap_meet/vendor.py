class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        #result = self.inventory.pop(self.inventory.index(item))
        self.inventory.remove(item)
        return item
        
    def get_by_category(self, category_name):
        category = []
        if not category_name:
            return category

        # for i in self.inventory:
        #     if category_name == i.category:
        #         category.append(i)

        category = [i for i in self.inventory if i.category == category_name]
        return category

    def swap_items(self, vendor, my_item, their_item):
        other_vendor = vendor

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        their_swap = other_vendor.remove(their_item)
        my_swap = self.remove(my_item)

        self.add(their_swap) and other_vendor.add(my_swap)

        return True

    def swap_first_item(self, vendor):
        other_vendor = vendor

        if not self.inventory or not other_vendor.inventory:
            return False

        my_first_item = self.inventory[0]
        thier_first_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first_item, thier_first_item)
        

    def get_best_by_category(self, category):
        
        category = category.capitalize()

        best_condition = 0
        best_item = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item


        return best_item
        
#         items_matching_cat = [item for item in self.inventory if item.category == category]
    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        other - the other vendor
        my_priority = the category vendor wants to receive
        their_priority = category other vendor wants to recive
        """
        if not self.get_best_by_category(their_priority) and not other.get_best_by_category(my_priority):
            return False

        thier_priority_from_my_inv = self.get_best_by_category(their_priority)
        my_priority_from_their_inv = other.get_best_by_category(my_priority)
        

        return self.swap_items(other, thier_priority_from_my_inv, my_priority_from_their_inv)

        
        



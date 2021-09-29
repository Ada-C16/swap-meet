class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
        
    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.remove(my_item)
            friend.inventory.append(my_item)
            friend.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False
    
    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            friend.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            self.inventory.append(friend.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self, category):
        # get list of items with matching categories
        matched_categories = []
        for item in self.inventory:
            if item.category == category:
                matched_categories.append(item)

        if not matched_categories:
            return None
        else:
            best_condition = 0
            best_item = matched_categories[0]
            for matched_item in matched_categories:
                if matched_item.condition > best_condition:
                    best_condition = matched_item.condition
                    best_item = matched_item
                else:
                    pass
            return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        items_to_swap_from_other = []
        for item in other.inventory:
            if item.category == my_priority:
                items_to_swap_from_other.append(item)
            else:
                pass
        
        items_to_swap_for_other = []
        for item in self.inventory:
            if item.category == their_priority:
                items_to_swap_for_other.append(item)
            else:
                pass
        
        if not items_to_swap_from_other or not items_to_swap_for_other:
            return False
        else:
            best_item_in_other = items_to_swap_from_other[0]
            other_best_condition = 0
            for item in items_to_swap_from_other:
                if item.condition > other_best_condition:
                    other_best_condition = item.condition
                    best_item_in_other = item
                else:
                    pass

            best_item_in_mine = items_to_swap_for_other[0]
            my_best_condition = 0
            for item in items_to_swap_for_other:
                if item.condition > my_best_condition:
                    my_best_condition = item.condition
                    best_item_in_mine = item
                else:
                    pass

            other.inventory.remove(best_item_in_other)
            self.inventory.append(best_item_in_other)
            self.inventory.remove(best_item_in_mine)
            other.inventory.append(best_item_in_mine)

            return True



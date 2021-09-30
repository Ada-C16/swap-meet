from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item:Item) -> Item:
        self.inventory.append(item)
        return item

    def remove(self, item:Item) -> list or bool:
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category:str)->list:
        list_of_items_with_specific_category = []
        for each_item in self.inventory:
            if each_item.category == category:
                list_of_items_with_specific_category.append(each_item)
        return list_of_items_with_specific_category
    
    def swap_items(self, other, my_item: Item, their_item: Item)->bool:
        if my_item not in self.inventory or their_item not in other.inventory:
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            other.add(my_item)
            other.remove(their_item)
            return True

    def swap_first_item(self, other)->bool:
        if not self.inventory or not other.inventory:
            return False
        else:
            self.swap_items(other, self.inventory[0], other.inventory[0] )
            return True

            
    def get_best_by_category(self, category:str)->Item:
        temp_highest_condition = 0
        product_with_highest_condition = None
        for each_item in self.inventory:
            if each_item.condition > temp_highest_condition and each_item.category == category:
                temp_highest_condition = each_item.condition
                product_with_highest_condition = each_item
        return product_with_highest_condition
    
    def swap_best_by_category(self, other, my_priority:str=None, their_priority:str=None) -> bool:
        my_best_item_with_their_priority = self.get_best_by_category(their_priority)
        their_best_item_with_my_priority = other.get_best_by_category(my_priority)
        if my_best_item_with_their_priority and their_best_item_with_my_priority:
            self.swap_items(other,my_best_item_with_their_priority, their_best_item_with_my_priority)
            return True
        return False

    def swap_by_newest_with_age_limit(self, other, my_age_limit, their_age_limit):         # optional
        my_newest_item = self.helper_func_get_newest_item()
        their_newest_item = other.helper_func_get_newest_item()
        if my_newest_item and their_newest_item:
            if my_newest_item.age <= their_age_limit and their_newest_item.age <= my_age_limit:
                self.swap_items(other, my_newest_item, their_newest_item)
                return True
        return False

    def helper_func_get_newest_item(self):   # helper func for optional enhancement 
        if self.inventory:
            temp_min_age_my_item = self.inventory[0].age
            my_newest_item = self.inventory[0]
            for each_item in self.inventory:
                if each_item.age < temp_min_age_my_item:
                    temp_min_age_my_item = each_item.age
                    my_newest_item = each_item
            return my_newest_item
        return False
    
    


    


        
        

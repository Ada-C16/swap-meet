from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
        self.item = Item()

    def add(self, item):
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

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        if my_item in self.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
        if their_item in vendor.inventory:
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True

    def swap_first_item(self, another_vendor):
        if len(self.inventory) != 0 and len(another_vendor.inventory) != 0:
            # if self.inventory[0] and another_vendor.inventory[0]:
            another_vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            self.inventory.append(another_vendor.inventory[0])
            another_vendor.inventory.remove(another_vendor.inventory[0])
            return True
        else:
            return False


    def get_best_by_category(self, category):
        self.category = category
        item_with_max_condition = None 
        for item in self.inventory:
            # if item.condition > max_condition:
            # if item.category == category and item.condition > item_with_max_condition.condition and(if item_with_max_condition == None or item_with_max_condition.condition > item):
            if item.category == category:
                if item_with_max_condition == None:
                    item_with_max_condition = item
                if item.condition > item_with_max_condition.condition:
                    item_with_max_condition = item
        return item_with_max_condition
            
                

    def swap_best_by_category(self,other,my_priority,their_priority):
        best_item = self.get_best_by_category(category =their_priority)
        other_best_item = other.get_best_by_category(category =my_priority)
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False
        return self.swap_items(other, best_item, other_best_item)

# if self.vendor.item != their_priority:
        #     return False

        # if self.inventory == their_priority.category:
            #     return True

   
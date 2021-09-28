class Vendor:
    
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False

    def get_by_category(self, category):
        result = []
        for thing in self.inventory:
            if thing.category == category:
                result.append(thing)
        return result

    def swap_items(self, other_vendor, self_item, other_vendor_item):
        if self_item in self.inventory and other_vendor_item in other_vendor.inventory:
            self.add(other_vendor_item)
            other_vendor.remove(other_vendor_item)
            other_vendor.add(self_item)
            self.remove(self_item)
            return True
        else:
            return False
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) >= 1 and len(other_vendor.inventory) >= 1:
            return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        else:
            return False

    def get_best_by_category(self, selected_category):
        result = None
        item_list = self.get_by_category(selected_category)
        best_score = 0
        for item in item_list:
            if item.condition >= best_score:
                best_score = item.condition
                result = item
        return result

    def swap_best_by_category(self, other = None, my_priority = "", their_priority = ""):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        if not ( my_item and their_item ):
            return False
        else:
            return self.swap_items(other,my_item, their_item)

    def swap_by_newest(self, other = None):
        if len(self.inventory) < 1 or len(other.inventory) < 1:
            return False
        else:
            my_youngest_item = self.inventory[0]
            their_youngest_item = other.inventory[0]
            for my_item in self.inventory:
                if my_item.age < my_youngest_item.age:
                    my_youngest_item = my_item
            for their_item in other.inventory:
                if their_item.age < their_youngest_item.age:
                    their_youngest_item = their_item

            return self.swap_items(other, my_youngest_item, their_youngest_item)


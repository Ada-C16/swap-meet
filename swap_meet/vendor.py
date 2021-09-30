from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else[]
        self.item = Item()

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, new_item):
        if new_item in self.inventory:
            self.inventory.remove(new_item)
            if new_item not in self.inventory:
                return new_item
        elif new_item not in self.inventory:
            return False

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
            
        else:
            other_vendor.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            return True
    
    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True

    def get_best_by_category(self, category =""):
        items_by_category = self.get_by_category(category)
        if len(items_by_category) == 0:
            return None
        return max(items_by_category, key=lambda item: item.condition)
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        best_item = self.get_best_by_category(category=their_priority)
        their_best_item = other.get_best_by_category(category=my_priority)
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False
        return self.swap_items(other, best_item, their_best_item)

    # def get_by_age(self, age):
    #     items = []
    #     for item in self.inventory:
    #         if item.age == age:
    #             items.append(item)
    #     return items
    
    def get_newest_item(self, age = ""):
        items_by_age = self.get_by_category(age)
        if len(items_by_age) == 0:
            return None
        return min(items_by_age, key=lambda item: item.age)
    
    def swap_by_newest(self, other, my_item, their_item):
        my_newest = self.get_newest_item(age=my_item)
        their_newest = self.get_newest_item(age=their_item)
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False
        return self.swap_items(other, my_newest, their_newest)
from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory=[]):
        self.inventory = inventory 

    def add(self, item):
        #self.item = item
        self.inventory.append(item)
        return item

    def remove(self, item):
        #self.item = item
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        else: 
            return False

    def get_by_category(self, category):
        list_of_categories = []
        for item in self.inventory:
            if item.category == category:
                list_of_categories.append(item)
        return list_of_categories

    def swap_items(self, other_vendor, my_item, their_item): 
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.remove(their_item)
            self.inventory.append(their_item)
            return True
    
    def swap_first_item(self, friendor):
        # my_first_item = self.inventory[0]
        # their_first_item = friendor.inventory[0]
        #for item in self.inventory:
        #if self.inventory or friendor.inventory == [""]:
            #return False
        #else:
        if len(self.inventory) != 0 and len(friendor.inventory) != 0:
            friendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            self.inventory.append(friendor.inventory[0])
            friendor.remove(friendor.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self, category = ""):
        items_by_category = self.get_by_category(category)
        if len(items_by_category) == 0: 
            return None
        #best_condition = max(items_by_category)
        # best_in_category = {}
        # for item in self.inventory:
        #     if category == item.category:
        #         best_in_category[item] = item.category

        # print("********")
        # print(best_in_category)
        # max(best_in_category, key = lambda item: best_in_category[item])

        # print(")))))))")
        # print(max(best_in_category, key = lambda item: best_in_category[item]))

        return max(items_by_category, key = lambda item: item.condition)

    def swap_best_by_category(self, other, their_priority, my_priority):
        best_item = self.get_best_by_category(category = their_priority)
        their_best_item = other.get_best_by_category(category = my_priority)
        if len(self.inventory) != 0 and len(other.inventory) != 0: #and my_priority == their_priority they don't need to match categories 
            return self.swap_items(other, best_item, their_best_item)
        else:
            return False

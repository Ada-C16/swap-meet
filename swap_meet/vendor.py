
class Vendor():
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []

        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        return False 

    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, vendor, my_item, their_item):
        if len(self.inventory) == 0 or len(vendor.inventory)== 0: 
            return False 
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.remove(my_item)
        vendor.add(my_item)
        self.add(their_item)
        vendor.remove(their_item)    
        return True

    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        first_item = self.inventory[0]
        friends_first_item = vendor.inventory[0]
        result = self.swap_items(vendor, first_item, friends_first_item)
        return result

    def get_best_by_category(self, category):
        highest_condition = 0
        best_item = ""
        category_list = self.get_by_category(category)
        if len(category_list) == 0:
            return None
        for item in category_list:
            if item.condition > highest_condition:
                highest_condition = item.condition
                best_item = item 
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        #the best_item that matches their_priority
        my_best_item = self.get_best_by_category(their_priority)
        others_best_item = other.get_best_by_category(my_priority)

        if my_best_item and others_best_item:
            self.swap_items(other,my_best_item, others_best_item)
            return True 
        return False 

# Optional Enhancements
    def get_newest_item(self):
        if len(self.inventory) == 0:
            return False 
        newest_item = self.inventory[0]
        min_age = self.inventory[0].age
        for index in range(len(self.inventory)):
            if self.inventory[index].age <  min_age:
                min_age = self.inventory[index].age
                newest_item = self.inventory[index]
        return newest_item

    def swap_by_newest(self, other):
        others_newest_item = other.get_newest_item()
        result = self.swap_items(other, self.get_newest_item(), others_newest_item)
        return result 


        



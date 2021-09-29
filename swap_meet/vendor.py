from swap_meet.item import Item


class Vendor(Item):
    def __init__(self,inventory = None):
        if not inventory:
            inventory = []
        self.inventory= inventory
        super().__init__(category= "",condition = 0)
    
    
    def add(self,item):
        self.inventory.append(item)
        return item


    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False


    def get_by_category(self,category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self,friend_vendor,my_item,their_item):
        if my_item not in self.inventory or their_item not in friend_vendor.inventory:
            return False

        self.inventory.remove(my_item)
        friend_vendor.inventory.append(my_item)
        
        friend_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True
        
    
    
    def swap_first_item(self,friend_vendor):
        if len(self.inventory)== 0 or len(friend_vendor.inventory) == 0:
            return False
        my_item =self.inventory.pop(0)

        friend_item = friend_vendor.inventory.pop(0)
        self.inventory.append(friend_item)
        friend_vendor.inventory.append(my_item)
        return True


    def get_best_by_category(self,category):
        max_condition = 0
        quality_item = ""
        category_list = self.get_by_category(category)
        if len(category_list) == 0:
            return None

        for item in category_list:
            if item.condition > max_condition:
                max_condition = item.condition
                quality_item = item
        return quality_item

    def swap_best_by_category(self,other, my_priority,their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
    
        if my_best_item and their_best_item:
            self.swap_items(other,my_best_item,their_best_item)
            # self.inventory.remove(my_best_item)
            # other.inventory.remove(their_best_item)
            # self.inventory.append(their_best_item)
            # other.inventory.append(my_best_item)
            return True
        return False

    def get_newest_item(self):
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

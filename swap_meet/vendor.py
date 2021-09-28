from swap_meet.item import Item

class Vendor:
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
        else:
            return False

    def get_by_category(self, category):
        items_by_category = []
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)

        return items_by_category

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            friend.remove(their_item)
            return True
        return False

    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            my_first_item = self.inventory[0]
            their_first_item = friend.inventory[0]

            self.swap_items(friend, my_first_item, their_first_item)

            return True
        return False
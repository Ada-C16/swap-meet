class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if not item in self.inventory:
            return False

        self.inventory.remove(item)

        return item

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)

        return items

    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in friend_vendor.inventory:
            self.inventory.remove(my_item)
            friend_vendor.inventory.append(my_item)
        
            friend_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
            
        return False

    def swap_first_item(self, friend_vendor):
        if not self.inventory or not friend_vendor.inventory:
            return False

        first_elem_self = self.inventory[0]
        first_elem_friend = friend_vendor.inventory[0]

        print(self.inventory[0])
        self.inventory[0] = first_elem_friend
        print(self.inventory[0])

        friend_vendor.inventory[0] = first_elem_self

        return True
        

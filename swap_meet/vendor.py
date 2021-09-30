class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

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
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, vendor, my_item, their_item):
        if their_item not in vendor.inventory or my_item not in self.inventory:
            return False
        else:
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            return True

    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        else:
            testing_1 = vendor.inventory[0]
            testing_2 = self.inventory[0]
            self.inventory.append(testing_1)
            vendor.inventory.append(testing_2)
            vendor.inventory.pop(0)
            self.inventory.pop(0)
            return True

    def get_best_by_category(self, category):
        best_quality = 0
        try:
            for item in self.inventory:
                if item.category == category:
                    if item.condition > best_quality:
                        best_quality = item.condition
                        best_item = item
            else:
                return best_item 
        except UnboundLocalError as err:
            return None

                

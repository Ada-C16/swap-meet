class Vendor:
    def __init__(self,inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
        # if inventory != None else inventory = []

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
        result = []
        for each in self.inventory:
            if each.category == category:
                result.append(each)
        return result

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            vendor.inventory.remove(their_item)
            vendor.inventory.append(my_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
            self.inventory.append(vendor.inventory[0])
            vendor.inventory.append(self.inventory[0])
            self.inventory.pop(0)
            vendor.inventory.pop(0)
            return True
        else:
            return False        

    def get_best_by_category(self, category):
        max_value = -1
        result = None
        for each in self.inventory:
            if each.category == category:
                if each.condition > max_value:
                    result = each
                    max_value = each.condition
        return result

    def swap_best_by_category(self, other, my_priority, their_priority):
        best_for_me = []
        highest_for_me = -1
        best_for_them = []
        highest_for_them = -1
        for each in self.inventory:
            if each.category == their_priority and each.condition > highest_for_them:
                highest_for_them = each.condition
                best_for_them = each
        for each in other.inventory:
            if each.category == my_priority and each.condition > highest_for_me:
                highest_for_me = each.condition
                best_for_me = each
        if best_for_me == [] or best_for_them == []:
            return False
        else:
            self.inventory.append(best_for_me)
            other.inventory.append(best_for_them)
            self.inventory.remove(best_for_them)
            other.inventory.remove(best_for_me)
            return True
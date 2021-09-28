class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        index_list = [i for (i, value) in enumerate(self.inventory) if value == item]
        if len(index_list) == 0:
            return False
        else:
            return self.inventory.pop(index_list[0])
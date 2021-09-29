class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        for i in range(len(self.inventory)):
            if self.inventory[i] == item:
                return self.inventory.pop(i)
        return False

    def get_by_category(self, category):
        return [item for item  in self.inventory if item.category == category]

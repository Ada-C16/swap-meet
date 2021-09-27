class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
        except:
            return False
        return item

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

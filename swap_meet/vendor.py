class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        result = self.inventory.pop(self.inventory.index(item))
        return result
    def get_by_category(self, category_name):
        category = []

        for i in self.inventory:
            if category_name == i.category:
                category.append(i)

        return category
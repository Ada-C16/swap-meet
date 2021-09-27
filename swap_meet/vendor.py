class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory or []

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, to_remove):
        if to_remove not in self.inventory:
            return False
        self.inventory.remove(to_remove)
        return to_remove
    
    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]
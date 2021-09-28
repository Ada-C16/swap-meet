class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory
    
    def add(self, item_to_add):
        self.inventory.append(item_to_add)
        return item_to_add

    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        #or maybe throw an error instead here?
        self.inventory.remove(item_to_remove)
        return item_to_remove

    

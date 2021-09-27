class Vendor:
    def __init__(self, inventory = None):
        if not inventory: 
            inventory = []
        self.inventory = inventory

    # Adding item to inventory.
    def add(self, item):
        self.inventory.append(item)
        return item
    
    # Removing item to inventory. Returning false if not in inventory.
    def remove(self, item): 
        if item not in self.inventory:
            return False 
        self.inventory.remove(item)
        return item
        

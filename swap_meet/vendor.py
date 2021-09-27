class Vendor:
    
    def __init__(self, inventory=None): # Set a default value
        if inventory is None: # Default value is falsy, so set to empty list
            self.inventory = []
        else:
            self.inventory = inventory # If inventory is given, set it equal to inventory attribute

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item

    
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

    def get_by_category(self, category):
        # Return a list of items that match category
        # The vendor has an inventory list of items which have categories attached
        items = [] # Creates empty list to return

        for item in self.inventory: # For each item in inventory list
            if item.category == category: # That item represents an Item instance, with a category attribute
                items.append(item) # Append the whole item to the list

        return items

    def swap_items(self, person, item_1, item_2):
        # Make self.inventory item replace itself with person.inventory item
        if item_1 in self.inventory and item_2 in person.inventory:
            self.remove(item_1)
            self.add(item_2)

            person.remove(item_2)
            person.add(item_1)

            return self.inventory
        else:
            return False

    def swap_first_item(self, person):
        if not self.inventory or not person.inventory:
            return False
        self.inventory.append(person.inventory[0])
        person.remove(person.inventory[0])

        person.inventory.append(self.inventory[0])
        self.remove(self.inventory[0])

        return True
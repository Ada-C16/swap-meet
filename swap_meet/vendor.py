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

    def swap_items(self, person, my_item, their_item):
        # Make self.inventory item replace itself with person.inventory item
        if my_item in self.inventory and their_item in person.inventory:
            self.remove(my_item)
            self.add(their_item)

            person.remove(their_item)
            person.add(my_item)

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

    def get_best_by_category(self, category):
        
        max_list = []
        
        for item in self.inventory:
            if item.category == category:
                # Return that instance
                max_list.append(item)

        if len(max_list) == 0:
            return None
        max_list.remove(min(max_list, key=lambda item: item.condition))

        return max(max_list, key=lambda item: item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        # Find the item with the best condition
        # Swap those items in each vendor instance's inventory

        my_swap_item = self.get_best_by_category(their_priority) # Finds highest one in mine
        their_swap_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_swap_item, their_swap_item)
class Vendor:
    """
    This is a class of one vendor & their inventory.
    Attributes:
        inventory: list of items of object type Item() or any of its subclasses
        name: name of vendor as a string
    """

    def __init__(self, inventory=None, name=""):
        """
        Constructor for Vendor class
        Paramaters:
            inventory: list of items of obejct type Item() or its subclasses
            name: name of vendor as string
        """
        self.inventory = inventory if inventory else []
        self.name = name

    def add(self, item):
        """
        Parameter:
            item: an item from self.inventory
        Result:
            Appends item to self.inventory and returns item
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        Parameter:
            item: an item from self.inventory
        Result:
            Removes item from self.inventory and returns item
            Returns False if item is not in self.inventory
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        """
        Parameter:
            category: a string matching one of the item categories in self.inventory
        Result:
            Returns a list of items in self.inventory of a specified category
        """
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other, my_item, their_item):
        """
        Parameters:
            other: a Vendor object
            my_item: an item in self.inventory
            their_item: an item in other.inventory
        Result:
            swaps my_item with their_item
            returns True if swap is successful
            returns False if either item does not exist
        """
        if my_item in self.inventory and their_item in other.inventory:
            self.remove(my_item)
            other.remove(their_item)

            self.add(their_item)
            other.add(my_item)

            return True
        return False

    def swap_first_item(self, other):
        """
        Parameter:
            other: a Vendor object
        Result:
            swaps the first item from self.inventory with the first item from other.inventory
            Returns True on successful swap
            Returns False on failed swap
        """
        if self.inventory and other.inventory:
            return self.swap_items(other, self.inventory[0], other.inventory[0])
        return False

    def get_best_by_category(self, category):
        """
        Parameter:
            category: a string matching on of the item categories in self.inventory
        Result:
            Returns the item with the highest condition of the specified category from self.inventory
            Returns None if no item of the category exists
        """
        items = self.get_by_category(category)
        return max(items, key=lambda item: item.condition, default=None)

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Parameters:
            other: a Vendor object
            my_priority: a string matching one of the item categories in other.inventory
            their_priority: a string matching one of the item categories in self.inventory
        Result:
            Swaps the items from each vendor's inventory with the highest condition of the specified categories.
        """
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_item, their_item)

    def get_newest_item(self):
        """
        Result:
            Returns the item in self.inventory with the lowest age
            Returns None if no items have an age
        """
        items = [item for item in self.inventory if item.age != None]
        return min(items, key=lambda item: item.age, default=None)

    def swap_by_newest(self, other):
        """
        Parameter:
            other: a Vendor object
        Result:
            swaps the two items in self.inventory and other.invetory with the lowest ages
        """
        my_item = self.get_newest_item()
        their_item = other.get_newest_item()
        return self.swap_items(other, my_item, their_item)

    def print_inventory(self):
        """
        Result:
            prints out a list of the vendor's items
        """
        print(f"    - {self.name}'s Inventory:")
        for item in self.inventory:
            print(f"        - {item.name}")
            print(f"            - category: {item.category}")
            print(f"            - condition: {item.condition}")
            print(f"            - age: {item.age}")

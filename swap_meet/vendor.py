from swap_meet.item import Item

# Wave 1
"""The class vendor takes in a parameter of inventory. It has a method function
    that adds and removes items.
    Returns:
      It returns the item or the boolean false.
        """


class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
        self.item = Item()

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
# Wave 2
        """This method checks through the items csategory and appends it to a list.
        """

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
# Wave 3
        """This item checks to see if an item is in my inventory or my friends
        and it removes it from my items to append to theirs. The same is done on
        their end.
        """

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        if my_item in self.inventory:
            self.remove(my_item)
            vendor.add(my_item)
        if their_item in vendor.inventory:
            vendor.remove(their_item)
            self.add(their_item)
            return True
# Wave 4
        """[summary]
        """

    def swap_first_item(self, another_vendor):
        if len(self.inventory) != 0 and len(another_vendor.inventory) != 0:
            another_vendor.add(self.inventory[0])
            self.remove(self.inventory[0])
            self.add(another_vendor.inventory[0])
            another_vendor.remove(another_vendor.inventory[0])
            return True
        else:
            return False
# Wave 6
        """This method gets each item based by its category. It also calculates
        the item with the best condition and returns it. The last method completes a switch
        based on the items category.
        """

    def get_best_by_category(self, category):
        self.category = category
        item_with_max_condition = None
        for item in self.inventory:
            if item.category == category:
                if item_with_max_condition == None:
                    item_with_max_condition = item
                if item.condition > item_with_max_condition.condition:
                    item_with_max_condition = item
        return item_with_max_condition

    def swap_best_by_category(self, other, my_priority, their_priority):
        best_item = self.get_best_by_category(category=their_priority)
        other_best_item = other.get_best_by_category(category=my_priority)
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False
        return self.swap_items(other, best_item, other_best_item)
# Wave 7 - Optional
        """This method finds the newest item in a list and returns it based
        on its index. The swap_by_newest index swaps my newest item with my
        friends newest item.
        """

    def find_newest_item(self):
        sort_age_list = sorted(self.inventory, key=lambda item: item.age)
        return sort_age_list[0]

    def swap_by_newest(self, other):
        my_newest_item = self.find_newest_item()
        their_new_item = other.find_newest_item()
        self.swap_items(other, my_newest_item, their_new_item)

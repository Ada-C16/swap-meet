from operator import attrgetter


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

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

    def swap_items(self, other, item_to_give, item_to_receive):
        if item_to_give not in self.inventory or item_to_receive not in other.inventory:
            return False
        other.add(self.remove(item_to_give))
        self.add(other.remove(item_to_receive))
        return True

    def swap_first_item(self, other):
        try:
            return self.swap_items(other, self.inventory[0], other.inventory[0])
        except IndexError:
            return False

    def get_best(self, items=None):
        """
        input: list of selected item objects (if not given, default to all item objects in inventory)
        output: object with the largest condition attribute value
        """
        if items is None:
            items = self.inventory
        try:
            return max(items, key=attrgetter("condition"))
        except ValueError:
            return None

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        return self.get_best(items_in_category)

    def swap_best_by_category(self, other, my_priority, their_priority):
        item_to_give = self.get_best_by_category(their_priority)
        item_to_receive = other.get_best_by_category(my_priority)
        return self.swap_items(other, item_to_give, item_to_receive)

    def get_newest(self, items=None):
        """
        input: list of selected item objects (if not given, default to all item objects in inventory)
        output: object with the smallest age attribute value
        """
        if items is None:
            items = self.inventory
        try:
            return min(items, key=attrgetter("category"))
        except ValueError:
            return None

    def swap_by_newest(self, other):
        item_to_give = self.get_newest()
        item_to_receive = other.get_newest()
        return self.swap_items(other, item_to_give, item_to_receive)

    def get_newest_by_category(self, category):
        items = self.get_by_category(category)
        return self.get_newest(items)

    def swap_newest_by_category(self, other, category):
        item_to_give = self.get_newest_by_category(category)
        item_to_receive = other.get_newest_by_category(category)
        return self.swap_items(other, item_to_give, item_to_receive)

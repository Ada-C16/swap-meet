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

    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory and their_item in other.inventory:
            other.add(self.remove(my_item))
            self.add(other.remove(their_item))
            return True
        return False

    def swap_first_item(self, other):
        my_first_item = next(iter(self.inventory), None)
        their_first_item = next(iter(other.inventory), None)
        return self.swap_items(other, my_first_item, their_first_item)

    def get_best_by_category(self, category):
        return max(
            self.get_by_category(category),
            default=None,
        )

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_best = other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        return self.swap_items(other, my_best, their_best)

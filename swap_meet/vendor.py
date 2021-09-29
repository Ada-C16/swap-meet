
class Vendor:
    def __init__(self, inventory=[]):
      self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
      if item in self.inventory:
        self.inventory.remove(item)
        return item
      else:
        return False

    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
          if item.category == category:
            items_list.append(item)
        return items_list

    def swap_items(self, another_vendor, my_item, their_item):
      if my_item not in self.inventory or their_item not in another_vendor.inventory:
        return False
      self.inventory.remove(my_item)
      another_vendor.inventory.remove(their_item)
      self.inventory.append(their_item)
      another_vendor.inventory.append(my_item)
      return True
      
    def swap_first_item(self, another_vendor):
      if len(self.inventory) == 0 or len(another_vendor.inventory) == 0:
        return False

      my_first_item = self.inventory[0]
      their_first_item = another_vendor.inventory[0]

      return self.swap_items(another_vendor, my_first_item, their_first_item)

    def get_best_by_category(self, category = ""):

        items_by_category = self.get_by_category(category)

        if len(items_by_category) == 0:
          return None
      
        return max(items_by_category, key = lambda item : item.condition)
  
    def swap_best_by_category(self, other, my_priority, their_priority):
      my_best_item = self.get_best_by_category(category = their_priority)

      their_best_item = other.get_best_by_category(category = my_priority)

      if len(self.inventory) == 0 or len(other.inventory) == 0:
        return False

      return self.swap_items(other, my_best_item, their_best_item)

    def swap_by_newest(self, other, my_item, their_item):
      pass
      newest_item = self.get_age(their_item)
      their_newest_item = other.get_age(my_item)



      



      






class Vendor:
  def __init__(self, inventory = None):
    self.inventory = inventory or []

  def add(self, item):
    self.inventory.append(item)
    return item

  def remove(self, item):
    if item not in self.inventory:
      return False
    self.inventory.remove(item)
    return item 

  def swap_items(self, other, my_item, their_item):
    if not (my_item in self.inventory and their_item in other.inventory):
       return False
    self.add(other.remove(their_item))
    other.add(self.remove(my_item))
    return True
  
  def swap_first_item(self, other):
    return self.swap_items(other, self.inventory[0], other.inventory[0]) if self.inventory and other.inventory else False
  
  def get_by_category(self, category):
    return [item for item in self.inventory if item.category == category]

  def get_best_by_category(self, category):
    return max(self.get_by_category(category), key = lambda a: a.condition, default = None)

  def swap_best_by_category(self, other, my_priority, their_priority):
    return self.swap_items(other, self.get_best_by_category(their_priority), other.get_best_by_category(my_priority))
  
  def get_newest_in_inventory(self):
    return min(self.inventory, key = lambda item : item.age, default = None)

  def swap_by_newest(self, other):
    return self.swap_items(other, self.get_newest_in_inventory(), other.get_newest_in_inventory())
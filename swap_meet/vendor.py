class Vendor:
  def __init__(self, inventory = None):
    if not inventory:
        inventory = []

    self.inventory = inventory

  def add(self, item):
    self.inventory.append(item)
    return item

  def remove(self, item):
    if item not in self.inventory:
      return False

    self.inventory.remove(item)
    return item


  def swap_items(self, vendor_2, my_item, their_item):
    if not (my_item in self.inventory and their_item in vendor_2.inventory):
      return False

    self.add(vendor_2.remove(their_item))
    vendor_2.add(self.remove(my_item))

    return True
  
  def swap_first_item(self, vendor_2):
    if not(self.inventory and vendor_2.inventory):
        return False
    return self.swap_items(vendor_2, self.inventory[0], vendor_2.inventory[0])
  
  def get_by_category(self, category):
    return [item for item in self.inventory if item.category == category]

  def get_best_by_category(self, category):
    return max(self.get_by_category(category), key = lambda a: a.condition, default = None)

  def swap_best_by_category(self, other, my_priority, their_priority):
    my_item = self.get_best_by_category(their_priority)
    their_item = other.get_best_by_category(my_priority)
    return self.swap_items(other, my_item, their_item)
  
  def get_newest_in_inventory(self):
    return min(self.inventory, key = lambda item : item.age, default = None)

  def swap_by_newest(self, vendor_2):
    my_item = self.get_newest_in_inventory()
    their_item = vendor_2.get_newest_in_inventory()
    return self.swap_items(vendor_2, my_item, their_item)
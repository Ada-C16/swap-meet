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

    vendor_2.inventory.insert(0, self.inventory.pop(self.inventory.index(my_item)))
    self.inventory.insert(0, vendor_2.inventory.pop(vendor_2.inventory.index(their_item)))
    return True
  

  def swap_first_item(self, vendor_2):
    if not(self.inventory and vendor_2.inventory):
        return False
    return self.swap_items(vendor_2, self.inventory[0], vendor_2.inventory[0])


  
  def get_by_category(self, category):

    return [item for item in self.inventory if item.category == category]

  def get_best_by_category(self, category):

      temp_list = self.get_by_category(category)

      return max(temp_list, key = lambda a: a.condition, default = None)
      

  def swap_best_by_category(self, other, my_priority, their_priority):

      my_item = self.get_best_by_category(their_priority)
      their_item = other.get_best_by_category(my_priority)

      return self.swap_items(other, my_item, their_item)
      
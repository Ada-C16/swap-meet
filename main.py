from swap_meet.vendor import Vendor
from swap_meet.item import Item

item_a = Item(category="clothing")
item_b = Item(category="clothing")
item_c = Item(category="clothing")
fatimah = Vendor(
    inventory=[item_a, item_b, item_c]
)

item_d = Item(category="electronics")
item_e = Item(category="decor")
jolie = Vendor(
    inventory=[item_d, item_e]
)

def swap_first_item(self, other_vendor):
    if len(self.inventory) == 0 or \
    len(other_vendor.inventory) == 0:
        return False
 
    my_item = self.inventory[0].category
    their_item = other_vendor.inventory[0].category

    self.swap_items(other_vendor, my_item, their_item)

fatimah.swap_first_item(jolie)

# this file is the driver for the source code written in the swap_meet directory
from swap_meet.item import Item
from swap_meet.vendor import Vendor

item_a = Item(category="furniture")

print(item_a)

item_a = Item(category="clothing")
item_b = Item(category="clothing")
item_c = Item(category="clothing")
khandice = Vendor(
    inventory=[item_a, item_b, item_c]
)

item_d = Item(category="electronics")
item_e = Item(category="decor")
alex = Vendor(
    inventory=[item_d, item_e]
)

result = khandice.swap_first_item(alex)

print(result)
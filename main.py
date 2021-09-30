# this file is the driver for the source code written in the swap_meet directory
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

item_a = Item(category="furniture")

# print(item_a)

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

# print(result)


pants = Clothing(5)
print(pants.condition)
print(pants.category)
print(pants.condition_description())

import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.vendor import Vendor
from swap_meet.item import Item

# Testing Wave 2, Case 1
# item_a = Item("clothing")
# item_b = Item("electronics")
# item_c = Item("clothing")

# vendor = Vendor(inventory = [item_a, item_b, item_c])
# print(vendor.inventory)
# item = vendor.get_by_category(item_a)
# print(item)

# Testing Wave 3, Case 2
# item_a = "clothing"
# item_b = "clothing"
# item_c = "clothing"
# fatimah = Vendor(
#     inventory=[item_a, item_b, item_c]
# )
# # print(fatimah.inventory)

# item_d = "electronics"
# item_e = "decor"
# jolie = Vendor(
#     inventory=[item_d, item_e]
# )
# # print(jolie.inventory)

# result = fatimah.swap_items(jolie, item_e, item_d)
# print(result)
# print(fatimah.inventory)
# print(jolie.inventory)

# Testing Wave 4
# item_a = Item(category="clothing")
# item_b = Item(category="clothing")
# item_c = Item(category="clothing")

# fatimah = Vendor(
#     inventory=[item_a, item_b, item_c]
# )
# print(fatimah.inventory)

# item_d = Item(category="electronics")
# item_e = Item(category="decor")

# jolie = Vendor(
#     inventory=[item_d, item_e]
# )
# print(jolie.inventory)
# result = fatimah.swap_first_item(jolie)
# print(f" after: {fatimah.inventory}")

# Testing Wave 5
# cloth = Clothing()
# print(cloth.category)
# print(str(cloth))

cloth = Clothing()
print(cloth.condition)

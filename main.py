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

# Testing Wave 6
# item_a = Clothing(condition=2.0)
# item_b = Decor(condition=2.0)
# item_c = Clothing(condition=4.0)
# item_d = Decor(condition=5.0)
# item_e = Clothing(condition=3.0)
# tai = Vendor(
#     inventory=[item_a, item_b, item_c, item_d, item_e]
# )

# # [item_a, item_c, item_e]
# best_item = tai.get_best_by_category("Clothing")
# print(best_item.condition)

# Testing Wave 6 Pt 2
item_a = Decor(condition=2.0)
item_b = Electronics(condition=4.0)
item_c = Decor(condition=4.0)
tai = Vendor(
    inventory=[item_a, item_b, item_c]
)

item_d = Clothing(condition=2.0)
item_e = Decor(condition=4.0)
item_f = Clothing(condition=4.0)
jesse = Vendor(
    inventory=[item_d, item_e, item_f]
)

result = tai.swap_best_by_category(
    other=jesse,
    my_priority="Clothing",
    their_priority="Decor"
)
for item in result:
    print(item.category)
    print(item.condition)
from vendor import Vendor
from item import Item
from clothing import Clothing
from decor import Decor
from electronics import Electronics

# testa = Vendor(["shoes", "hat", "spatula"])
# print(f"test 1 inventory: {testa.inventory}")

# testa2 = Vendor()
# print(f"test 2 inventory: {testa2.inventory}")

# item_a = Item(category="clothing")
# item_b = Item(category="electronics")
# item_c = Item(category="clothing")
# vendor = Vendor(inventory=[item_a, item_b, item_c])

# print(vendor.get_by_category("clothing"))

# print(item_b.category)

# print(item_a)

# tester = Clothing(condition=3.5)
# print(tester.category)
# print(tester.condition)
# print(tester.condition_description())

# items = [
#             Clothing(condition=5),
#             Decor(condition=5),
#             Electronics(condition=5)
#         ]

# print(items[0].condition_description())

# for item in items:
#     print(item.condition_description())

# items[0].condition = 1
# print(items[0].condition)

testthing = Clothing(condition = 5)
# print(testthing.condition)
# print(testthing.condition_description())
# testthing.condition = 4
# print(testthing.condition)
# print(testthing.condition_description())
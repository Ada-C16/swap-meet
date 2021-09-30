from swap_meet.vendor import Vendor
from swap_meet.item import Item


item_a = Item(age=0)
item_b = Item(age=3)
item_c = Item(age=2)
fatimah = Vendor(
    inventory=[item_a, item_b, item_c]
)

item_d = Item(age=5)
item_e = Item(age=4)
jolie = Vendor(
    inventory=[item_d, item_e]
)

result = fatimah.swap_by_newest(jolie)

assert len(fatimah.inventory) == 3
assert item_b not in fatimah.inventory
assert item_a in fatimah.inventory
assert item_c in fatimah.inventory
assert item_d in fatimah.inventory
assert len(jolie.inventory) == 2
assert item_d not in jolie.inventory
assert item_e in jolie.inventory
assert item_b in jolie.inventory
assert result

# item_a = Item(category="clothing")
# item_b = Item(category="clothing")
# item_c = Item(category="clothing")
# fatimah = Vendor(
#     inventory=[item_a, item_b, item_c]
# )

# item_d = Item(category="electronics")
# item_e = Item(category="decor")
# jolie = Vendor(
#     inventory=[item_d, item_e]
# )

# print("item b", id(item_b))
# print("item d", id(item_d))

# for inventory in fatimah.inventory:
#     print("fatimah", id(inventory))

# result = fatimah.swap_items(jolie, item_b, item_d)

for inventory in jolie.inventory:
    print("jolie", id(inventory))


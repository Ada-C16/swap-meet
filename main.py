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

print("item b", id(item_b))
print("item d", id(item_d))

for inventory in fatimah.inventory:
    print("fatimah", id(inventory))

result = fatimah.swap_items(jolie, item_b, item_d)

for inventory in jolie.inventory:
    print("jolie", id(inventory))
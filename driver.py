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

result = fatimah.swap_items(jolie, item_b, item_c)

print(result)

# assert len(fatimah.inventory) == 3
# assert item_d not in fatimah.inventory
# assert item_a in fatimah.inventory
# assert item_b in fatimah.inventory
# assert item_c in fatimah.inventory
# assert len(jolie.inventory) == 2
# assert item_d in jolie.inventory
# assert item_e in jolie.inventory
# assert not result
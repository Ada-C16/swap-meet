from swap_meet.vendor import Vendor
from swap_meet.item import Item

# item_a = Item(category="clothing")
# item_b = Item(category="electronics")
# item_c = Item(category="clothing")

# vendor_1 = Vendor(inventory = [item_b,item_b])
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

result = fatimah.swap_items(jolie, item_b, item_d)
print(len(result))

from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

item_a = Item(category="clothing")
item_b = Item(category="clothing")
item_c = Item(category="clothing")
fatimah = Vendor(inventory=[item_a, item_b, item_c])

item_d = Item(category="electronics")
item_e = Item(category="decor")
jolie = Vendor(inventory=[item_d, item_e])

result = fatimah.swap_first_item(jolie)

print(result)

print(fatimah.inventory[0].category)
print(jolie.inventory[0].category)

# print("--------------------")

# for i in jolie.inventory:
#     print(i.category)

from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item
# item_a = Clothing(condition=2.0)
# item_b = Decor(condition=2.0)
# item_c = Clothing(condition=4.0)
# item_d = Decor(condition=5.0)
# item_e = Clothing(condition=3.0)
# tai = Vendor(
#     inventory=[item_a, item_b, item_c, item_d, item_e]
# )
# print(item_a.condition, item_a.category)
# print(tai.get_best_by_category("Clothing"))

# assert best_item.category == "Clothing"
# assert best_item.condition == pytest.approx(4.0)


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

fatimah.swap_items(jolie, item_b, item_d)
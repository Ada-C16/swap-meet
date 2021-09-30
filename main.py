from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

item_a = Decor(age=2.0)
item_b = Electronics(age=4.0)
item_c = Decor(age=4.0)
tai = Vendor(
    inventory=[item_a, item_b, item_c]
)

item_d = Clothing(age=2.0)
item_e = Decor(age=4.0)
item_f = Clothing(age=4.0)
jesse = Vendor(
    inventory=[item_d, item_e, item_f]
)

result = tai.swap_by_newest(other=jesse)

print(result)
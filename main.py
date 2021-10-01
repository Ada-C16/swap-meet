from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


#Informal testing of get_newest_in_inventory and swap_by_newest


item_a = Decor(condition=2.0, age=0.3)
item_b = Electronics(condition=4.0, age=5.6)
item_c = Decor(condition=4.0, age=75.7)
tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

item_d = Clothing(condition=2.0, age=2.5)
item_e = Decor(condition=4.0, age=1.7)
item_f = Clothing(condition=0.3, age=50)
jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )


tessa = Vendor()

print(jesse.inventory[2].condition_description())
print(tessa.get_newest_in_inventory())
print(tessa.swap_by_newest(tai))
print(tai.swap_by_newest(jesse))
print(item_e in tai.inventory)
print(item_a in jesse.inventory)

from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.electronics import Electronics
from swap_meet.decor import Decor


item_a = Decor(age =2.0)
item_b = Electronics(age=4.0)
item_c = Decor(age = 4.0)
tai = Vendor(
    inventory=[item_c, item_b, item_a]
    )

item_d = Clothing(age=2.0)
item_e = Decor(age=4.0)
item_f = Clothing(age=4.0)
jesse = Vendor(
        inventory=[item_f, item_e, item_d])
        
result = tai.swap_by_newest(jesse,
                            my_newest_item= tai.get_new_item(),
                            friend_newest_item = jesse.get_new_item() ) 
print(item_a in jesse.inventory)
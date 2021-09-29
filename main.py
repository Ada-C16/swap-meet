from swap_meet.vendor import Vendor 
from swap_meet.item import Item 


item_a = Item("Decor", 5, 2)
item_b = Item("Decor", 2, 0)
vendor = Vendor([item_a, item_b])
print(*vendor.inventory)
item_c = Item("Decor", 3, 3)
vendor.add(item_c)
item_e = Item("Decor", 5, 1)
item_d = Item("Decor", 1, 5)
vendor_2 = Vendor([item_e, item_d])
print(*vendor_2.inventory)
vendor.swap_by_newest(vendor_2)
print(*vendor.inventory)
print(*vendor_2.inventory)




from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.swap_meet import SwapMeet

# knox's items
box = Item(name="box", condition=2, age=1, category="misc")
shoe = Clothing(name="shoe", condition=1, age=0)
tv = Electronics(name="tv", condition=4, age=4)
mirror = Decor(name="mirror", condition=3, age=50)
rose = Item(name="rose", condition=5, category="misc")

knox = Vendor([box, shoe, tv, mirror, rose], name="Knox")

# ryan's items
pen = Item(name="pen", condition=3, age=0, category="misc")
hat = Clothing(name="hat", condition=4, age=2)
tablet = Electronics(name="tablet", condition=3, age=1)
fake_plant = Decor(name="fake plant", condition=2, age=10)
tulip = Item(name="tulip", condition=5, category="misc")

ryan = Vendor([pen, hat, tablet, fake_plant, tulip], name="Ryan")

meet = SwapMeet([knox, ryan])

meet.print_welcome()

meet.print_vendor_inventories()


swap_option = meet.get_swap_type()

if swap_option == 1:
    knox.swap_by_newest(ryan)
elif swap_option == 2:
    knox.swap_first_item(ryan)
elif swap_option == 3:
    knox_category = meet.get_category_options(knox)
    ryan_category = meet.get_category_options(ryan)
    knox.swap_best_by_category(ryan, knox_category, ryan_category)

meet.print_vendor_inventories()

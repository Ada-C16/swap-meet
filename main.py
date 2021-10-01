from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


# todo: welcome message
# todo: ask for name
# todo:

box = Item(condition=2, age=1, category="misc")
shoe = Clothing(condition=1, age=0)
tv = Electronics(condition=4, age=4)
mirror = Decor(condition=5, age=50)

knox = Vendor([box, shoe, tv, mirror])
print(knox.inventory[0].age)

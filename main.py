from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

box = Item(condition=2, age=1, category="misc")
shoe = Clothing(condition=1, age=0)
tv = Electronics(condition=4, age=4)
mirror = Decor(condition=3, age=50)
rose = Item(condition=5)

knox = Vendor([box, shoe, tv, mirror, rose])
print(knox.get_newest_item())

pen = Item(condition=3, age=0, category="misc")
hat = Clothing(condition=4, age=2)
tablet = Electronics(condition=3, age=1)
fake_plant = Decor(condition=2, age=10)
tulip = Item(condition=5)


ryan = Vendor([pen, hat, tablet, fake_plant])
print(ryan.get_newest_item())

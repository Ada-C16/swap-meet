from swap_meet.vendor import Vendor 
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

radio = Item("electronics")
shirt = Clothing()
pan = Item("cookware")
shoes = Clothing()
earbuds = Item("electronics")

v1 = Vendor([radio, shirt, pan, shoes, earbuds])

v1.get_by_category("clothing")

pants = Clothing(age=3.5)
candlestick = Decor(age=3.5)
phone = Electronics(condition=3.5)

items = [
    pants,
    candlestick,
    phone
]
for item in items:
    print(item.condition)
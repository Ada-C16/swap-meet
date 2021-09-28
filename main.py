from swap_meet.vendor import Vendor 
from swap_meet.item import Item

radio = Item("electronics")
shirt = Item("clothing")
pan = Item("cookware")
shoes = Item("clothing")
earbuds = Item("electronics")

v1 = Vendor([radio, shirt, pan, shoes, earbuds])

print(v1.get_by_category("clothing"))
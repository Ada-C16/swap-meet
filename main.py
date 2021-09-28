from swap_meet.vendor import Vendor
from swap_meet.item import Item

item_a = Item(category="clothing")
item_b = Item(category="electronics")
item_c = Item(category="clothing")

vendor_1 = Vendor(inventory = [item_b,item_b])

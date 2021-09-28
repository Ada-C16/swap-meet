from swap_meet.item import Item
from swap_meet.vendor import Vendor

new_item = Item()
new_inventory = Vendor(inventory = ['a', 'b', 'c'])
print(new_inventory.inventory[0])
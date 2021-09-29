from swap_meet.vendor import Vendor
from swap_meet.item import Item

item_a = Item(category="clothing")
item_b = Item(category="clothing")
item_c = Item(category="clothing")
vendor = Vendor(
    inventory=[item_a, item_b, item_c]
)

items = vendor.get_by_category("electronics")

print(items)
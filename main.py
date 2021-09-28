
from swap_meet.vendor import Vendor
from swap_meet.item import Item

Item_1 = Item(category = "cosmetics")
Item_2 = Item(category = "clothing")
Item_3 = Item(category = "houseware")
Item_4 = Item(category = "houseware")

vendor1 = Vendor(inventory = [Item_1, Item_2, Item_3])
print(len(vendor1.inventory))
for each in vendor1.get_by_category("houseware"):
    print(each.category)

vendor1.add(Item_4)



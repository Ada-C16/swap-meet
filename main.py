
from swap_meet.clothing import Clothing
from swap_meet.electronics import Electronics
from swap_meet.vendor import Vendor
from swap_meet.item import Item

Item_1 = Item(category = "cosmetics")
Item_2 = Item(category = "clothing")
Item_3 = Item(category = "houseware")
Item_4 = Item(category = "houseware")
# vendor3 = Vendor()
# vendor3.inventory = [Item_1, Item_2, Item_3]

# # vendor3.inventory.extend([Item_1,Item_2,Item_3])
# print(len(vendor3.inventory))
# v =Clothing ()
# print(v.category)

# vendor1 = Vendor(inventory = [Item_1, Item_2, Item_3])
# print(len(vendor1.inventory))
# for each in vendor1.get_by_category("houseware"):
#     print(each.category)

# vendor1.add(Item_4)

vendor4 = Vendor(inventory = [Item_1, Item_2, Item_3])

print(len(vendor4.inventory))

vendor2 = Vendor()
print(len(vendor2.inventory))

vendor3 = Vendor()
vendor3.add(Item_4)
print(len(vendor2.inventory))

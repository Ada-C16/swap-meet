from swap_meet.vendor import Vendor 
from swap_meet.item import Item
from swap_meet.clothing import Clothing

item1 = Item("Clothing", 5)
item2 = Item("Electronics", 1)
item3 = Item("Clothing", 2)

item4 = Item("Decor", 5)
item5 = Item("Clothing", 4)
item6 = Item("Electronics", 2)

item1

# print(item1.category)
# print(item2.category)
# print(item3.category)

vendor1 = Vendor([item1, item2, item3])
other = Vendor([item4, item5, item6])

# print(vendor1.inventory)


cloth = Clothing(condition=3.5)
print(cloth.condition)

print(type(item1.condition))
print(f"This is my test: ") 
print(vendor1.swap_best_by_category(other, 'Decor', 'Clothing'))

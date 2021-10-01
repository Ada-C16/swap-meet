from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

items = [
    Clothing(condition=5),
    Decor(condition=5),
    Electronics(condition=5)
]
five_condition_description = items[2].condition_description()
print(five_condition_description)
# assert isinstance(five_condition_description, str)
# for item in items:
#     assert item.condition_description() == five_condition_description

# items[0].condition = 1
# one_condition_description = items[0].condition_description()
# assert isinstance(one_condition_description, str)

# for item in items:
#     item.condition = 1
#     assert item.condition_description() == one_condition_description

# assert one_condition_description != five_condition_description
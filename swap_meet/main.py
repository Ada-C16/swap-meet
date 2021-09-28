from vendor import Vendor
from item import Item
from clothing import Clothing
from electronics import Electronics

mac = Vendor()
other = Vendor()

shirt = Clothing(condition=5)
pants = Clothing(condition=4)
computer = Electronics(condition=3)
other.add(shirt)
other.add(pants)
mac.add(computer)

m = mac.swap_best_by_category(other, "Clothing", "Electronics")

print(m)

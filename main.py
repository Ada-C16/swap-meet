from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# knox's items
box = Item(name="box", condition=2, age=1, category="misc")
shoe = Clothing(name="shoe", condition=1, age=0)
tv = Electronics(name="tv", condition=4, age=4)
mirror = Decor(name="mirror", condition=3, age=50)
rose = Item(name="rose", condition=5, category="misc")

knox = Vendor([box, shoe, tv, mirror, rose], name="Knox")

# ryan's items
pen = Item(name="pen", condition=3, age=0, category="misc")
hat = Clothing(name="hat", condition=4, age=2)
tablet = Electronics(name="tablet", condition=3, age=1)
fake_plant = Decor(name="fake plant", condition=2, age=10)
tulip = Item(name="tulip", condition=5, category="misc")

ryan = Vendor([pen, hat, tablet, fake_plant, tulip], name="Ryan")

print("******************************")
print("Welcome to the Swap Meet!")
print("******************************")

print("")
print("")
print("Meet our vendors:")

knox.print_inventory()
ryan.print_inventory()

print("******************************")

swap_option = knox.get_swap_type()

if swap_option == 1:
    knox.swap_by_newest(ryan)
    knox.print_inventory()
elif swap_option == 2:
    knox.swap_first_item(ryan)
    knox.print_inventory()
elif swap_option == 3:
    print(
        "Categories: \n\
        1. misc \n\
        2. clothing\n\
        3. electronics\n\
        4. decor"
    )
    knox_category = int(
        input(
            "Choose a number from above to pick the category that Knox wants to recieve.\n"
        )
    )
    ryan_category = int(
        input(
            "Choose a number from above to pick the category that Ryan wants to receive.\n"
        )
    )

    if knox_category == 1:
        knox_category = "misc"
    elif knox_category == 2:
        knox_category = "Clothing"
    elif knox_category == 3:
        knox_category = "Electronics"
    elif knox_category == 4:
        knox_category == "Decor"

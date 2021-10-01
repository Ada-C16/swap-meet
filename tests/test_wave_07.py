import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    item_a = Clothing(age=5)
    item_b = Decor(age=1)
    item_c = Electronics(age=3)
    Veronica = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Decor(age=6)
    Yvette = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    Veronica.swap_by_newest(Yvette)

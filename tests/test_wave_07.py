import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def swap_by_newest(self, other):
    item_a = Decor(age = 1.0)
    item_b = Electronics(age = 4.0)
    item_c = Decor(age = 3.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age = 2.0)
    item_e = Decor(age = 1.0)
    item_f = Clothing(age = 4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    result = tai.swap_by_newest(
        other=jesse,
        )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    item_a = Decor(age=5)
    item_b = Electronics(age=1)
    item_c = Decor(age=2)
    tiffany = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=8)
    item_e = Decor(age=13)
    item_f = Clothing(age=15)
    karishma = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tiffany.swap_by_newest(
        other=karishma
    )

    assert result
    assert len(tiffany.inventory) == 3
    assert len(karishma.inventory) == 3
    assert item_a in tiffany.inventory
    assert item_b not in tiffany.inventory
    assert item_c in tiffany.inventory
    assert item_d in tiffany.inventory
    assert item_d not in karishma.inventory
    assert item_e in karishma.inventory
    assert item_f in karishma.inventory
    assert item_b in karishma.inventory

import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_by_newest():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=4.0)
    item_d = Decor(age=5.0)
    item_e = Clothing(age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_by_newest()

    assert newest_item.category == "Clothing"
    assert newest_item.age == pytest.approx(2.0)

def test_get_by_newest_no_inventory_return_none():
    tai = Vendor(
        inventory=[]
    )

    newest_item = tai.get_by_newest()

    assert newest_item is None


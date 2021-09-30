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

def test_get_by_newest_some_items_with_None_age():
    item_a = Clothing(age=1)
    item_b = Decor(age=None)
    item_c = Electronics(age=None)
    item_d = Clothing(age=5)
    bean = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    newest_item = bean.get_by_newest()

    assert newest_item.category == "Clothing"
    assert newest_item.age == 1

def test_get_by_newest_empty_inventory():
    jeff = Vendor(
        inventory=[]
    )

    newest_item = jeff.get_by_newest()

    assert newest_item == None

def test_swap_by_newest():
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        other=jesse
    )

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert item_d not in jesse.inventory
    assert item_a not in tai.inventory

def test_swap_by_newest_inventory_empty_is_false():
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    jeff = Vendor(
        []
    )
    bean = Vendor(
        [item_a, item_b, item_c]
    )

    result = test_swap_by_newest()

    assert not result
    assert len(jeff.inventory) == 0
    assert len(bean.inventory) == 3
    assert item_a in bean.inventory
    assert item_b in bean.inventory
    assert item_c in bean.inventory

def test_swap_by_newest_first_youngest_if_tie():
    item_a = Decor(age=5.0)
    item_b = Electronics(age=2.0)
    item_c = Decor(age=2.0)
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    bean = Vendor(
        [item_a, item_b, item_c]
    )
    jeff = Vendor(
        [item_d, item_e, item_f]
    )

    bean.swap_by_newest(jeff)

    assert len(jeff.inventory) == 3
    assert len(bean.inventory) == 3
    assert item_a in bean.inventory
    assert item_b in jeff.inventory
    assert item_c in bean.inventory
    assert item_d in bean.inventory
    assert item_e in jeff.inventory
    assert item_f in jeff.inventory
    assert item_b not in bean.inventory
    assert item_d not in jeff.inventory


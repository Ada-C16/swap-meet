from typing import AsyncGenerator
import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_get_newest():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=1.0)
    item_c = Clothing(age=4.0)
    item_d = Decor(age=5.0)
    item_e = Clothing(age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_newest()

    assert best_item.age == pytest.approx(1.0)


def test_get_newest_with_duplicates():
    item_a = Clothing(age=2.0)
    item_b = Clothing(age=2.0)
    item_c = Clothing(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_newest()

    assert best_item.age == pytest.approx(2.0)


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
        friend=jesse
    )

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a not in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory
    assert item_d not in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert item_a in jesse.inventory


def test_swap_by_newest_reordered():
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    result = tai.swap_by_newest(
        friend=jesse
    )

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a not in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory
    assert item_d not in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert item_a in jesse.inventory


def test_swap_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest(
        friend=jesse
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_by_newest_no_friend_inventory_is_false():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest(
        friend=jesse
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_items_have_age_as_float():
    items = [
        Clothing(age = 3.5),
        Decor(age = 3.5),
        Electronics(age = 3.5)
    ]
    for item in items:
        assert item.age == pytest.approx(3.5)

def test_get_newest_item():
    item_a = Item(age = 3.5)
    item_b = Item(age = 1.5)
    item_c = Item(age = 7)
    claire = Vendor(
        inventory = [item_a, item_b, item_c]
    )

    result = claire.get_newest_item()

    assert result == item_b
    assert result.age == pytest.approx(1.5)

def test_get_newest_return_false_if_empty_inventory():
    ansel = Vendor(
        inventory = []
    )

    result = ansel.get_newest_item()

    assert not result

def test_get_newest_returns_first_if_two_newest_exists():
    item_a = Item(age = 3.5)
    item_b = Item(age = 1.5)
    item_c = Item(age = 1.5)
    trenisha = Vendor(
        inventory = [item_a, item_b, item_c]
    )

    result = trenisha.get_newest_item()

    assert result == item_b

def test_swap_by_newest():
    item_a = Item(age = 3.0)
    item_b = Item(age = 4.0)
    item_c = Item(age = 1.0)
    stephanie = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age = 7.0)
    item_e = Item(age = 3.5)
    item_f = Item(age = 1.5)
    jeff = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = stephanie.swap_by_newest(jeff)

    assert len(stephanie.inventory) == 3
    assert item_c not in stephanie.inventory
    assert item_b in stephanie.inventory
    assert item_a in stephanie.inventory
    assert item_f in stephanie.inventory
    assert len(jeff.inventory) == 3
    assert item_f not in jeff.inventory
    assert item_d in jeff.inventory
    assert item_e in jeff.inventory
    assert item_c in jeff.inventory
    assert result

def test_swap_by_newest_returns_false_if_inventory_is_empty():
    stephanie = Vendor(
        inventory = []
    )

    item_d = Item(age = 7.0)
    item_e = Item(age = 3.5)
    item_f = Item(age = 1.5)
    jeff = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = stephanie.swap_by_newest(jeff)

    assert len(stephanie.inventory) == 0
    assert len(jeff.inventory) == 3
    assert not result

def test_swap_by_newest_returns_false_if_other_inventory_is_empty():
    item_a = Item(age = 3.0)
    item_b = Item(age = 4.0)
    item_c = Item(age = 1.0)
    stephanie = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jeff = Vendor(
        inventory = []
    )

    result = stephanie.swap_by_newest(jeff)

    assert len(stephanie.inventory) == 3
    assert len(jeff.inventory) == 0
    assert not result
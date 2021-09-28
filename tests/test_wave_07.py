import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    item_a = Clothing(condition=2.0, age = 5)
    item_b = Decor(condition=2.0, age = 2)
    item_c = Clothing(condition=4.0, age = 100)
    item_d = Decor(condition=5.0, age = 7)
    item_e = Clothing(condition=3.0, age = 3)
    item_f = Electronics(condition = 0.0, age = 98)
    devin = Vendor(inventory=[item_a, item_b, item_c,])
    renee = Vendor(inventory = [item_d, item_e, item_f])

    result = devin.swap_by_newest(renee)

    assert result
    assert item_b in renee.inventory
    assert item_b not in devin.inventory
    assert item_e in devin.inventory
    assert item_e not in renee.inventory
    assert len(renee.inventory) == 3
    assert len(devin.inventory) == 3

def test_swap_by_newest_empty_inventory_is_false():
    devin = Vendor()
    renee = Vendor()

    result = devin.swap_by_newest(renee)

    assert not result

def test_swap_by_newest_items_with_same_age_swaps_first_item_of_that_age():
    item_a = Clothing(condition=2.0, age = 5)
    item_b = Decor(condition=2.0, age = 2)
    item_c = Clothing(condition=4.0, age = 2)
    item_d = Decor(condition=5.0, age = 7)
    item_e = Clothing(condition=3.0, age = 3)
    item_f = Electronics(condition = 0.0, age = 3)
    devin = Vendor(inventory=[item_a, item_b, item_c,])
    renee = Vendor(inventory = [item_d, item_e, item_f])

    result = devin.swap_by_newest(renee)

    assert result
    assert item_b not in devin.inventory
    assert item_c in devin.inventory
    assert item_b in renee.inventory
    assert item_e not in renee.inventory
    assert item_f in renee.inventory
    assert item_e in devin.inventory
    assert len(devin.inventory) == 3
    assert len(renee.inventory) == 3

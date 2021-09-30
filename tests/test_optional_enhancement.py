from swap_meet.item import Item
import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    item_a = Item(age=5)
    item_b = Item(age=3)
    item_c = Item(age=15)
    item_d = Item(age=50)
    item_e = Item(age=20)

    john = Vendor([item_a,item_c,item_e])
    mary = Vendor([item_b, item_d])

    swap_result = john.swap_by_newest_with_age_limit(other = mary, my_age_limit = 15, their_age_limit = 10)

    assert swap_result
    assert item_b in john.inventory
    assert item_a in mary.inventory
    assert item_a not in john.inventory
    assert item_b not in mary.inventory
    assert item_c, item_e in john.inventory
    assert item_d in mary.inventory


def test_swap_by_newest_with_one_empty_inventory_list():
    item_a = Item(age=5)
    item_b = Item(age=3)
    item_c = Item(age=15)
    item_d = Item(age=50)
    item_e = Item(age=20)

    john = Vendor([item_a,item_c,item_e])
    mary = Vendor([])

    swap_result = john.swap_by_newest_with_age_limit(other = mary, my_age_limit = 15, their_age_limit = 10)

    assert not swap_result
    assert len(john.inventory) == 3
    assert len(mary.inventory) == 0
    assert item_a and item_c and item_e in john.inventory




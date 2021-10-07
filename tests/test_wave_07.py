import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_age_is_valid():
    item = Clothing(age=1)
    assert item.age_description() == "This is pretty new! Nice!"
    item = Electronics(age=-1)
    assert item.age_description() == "This...should not be for sale"
    item = Decor(age=100)
    assert item.age_description() == "This is an antique!"

def test_get_by_age_returns_age():
    item_a = Clothing(age=3)
    item_b = Clothing(age=56)
    item_c = Clothing(age=15)
    item_d = Clothing(age=27)
    alice = Vendor(
        inventory = [item_a, item_b, item_c, item_d]
        )
    item_wanted = alice.get_by_age(56)
    assert item_wanted.age == 56
    
def test_get_by_newest_returns_min_age():
    item_a = Clothing(age=27)
    item_b = Clothing(age=56)
    item_c = Clothing(age=3)
    item_d = Clothing(age=15)
    alice = Vendor(
        inventory = [item_a, item_b, item_c, item_d]
        )
    item_wanted = alice.get_by_newest()
    assert item_wanted == item_c

def test_swap_by_newest_swaps_min_age_items_in_inventories():
    item_a = Clothing(age=27)
    item_b = Clothing(age=56)
    item_c = Electronics(age=3)
    item_d = Clothing(age=15)
    item_e = Decor()
    item_f = Electronics(age=1)
    alice = Vendor(
        inventory = [item_a, item_c, item_d]
        )
    hatter = Vendor(
        inventory = [item_b, item_e, item_f]
    )
    alice.swap_by_newest(hatter)
    assert item_e in alice.inventory
    assert item_c in hatter.inventory
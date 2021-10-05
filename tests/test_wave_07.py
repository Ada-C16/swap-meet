import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_get_newest_item():
    item_a = Clothing(age=10.0)
    item_b = Decor(age=10.0)
    item_c = Clothing(age=2.0)
    item_d = Decor(age=1.0)
    item_e = Clothing(age=5.0)
    michelle = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = michelle.get_newest_item("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.age == pytest.approx(2.0)


def test_get_newest_item_no_matches_is_none():
    item_a = Decor(age=10.0)
    item_b = Decor(age=10.0)
    item_c = Decor(age=4.0)
    michelle = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = michelle.get_newest_item("Electronics")

    assert best_item is None


def test_get_newest_item_with_duplicates():
    item_a = Clothing(age=2.0)
    item_b = Clothing(age=4.0)
    item_c = Clothing(age=4.0)
    michelle = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = michelle.get_newest_item("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.age == pytest.approx(2.0)


# def test_swap_by_newest():
#     item_a = Decor(age=2.0)
#     item_b = Electronics(age=4.0)
#     item_c = Decor(age=4.0)
#     michelle = Vendor(
#         inventory=[item_a, item_b, item_c]
#     )

#     item_d = Clothing(age=2.0)
#     item_e = Decor(age=4.0)
#     item_f = Clothing(age=4.0)
#     ivette = Vendor(
#         inventory=[item_d, item_e, item_f]
#     )

#     result = michelle.swap_by_newest(
#         other=ivette,
#         my_item="Clothing",
#         their_item="Decor"
#     )

#     assert result
#     assert len(michelle.inventory) == 3
#     assert len(ivette.inventory) == 3
#     assert item_a in michelle.inventory
#     assert item_b in michelle.inventory
#     assert item_c not in michelle.inventory
#     assert item_f in michelle.inventory
#     assert item_d in ivette.inventory
#     assert item_e in ivette.inventory
#     assert item_f not in ivette.inventory
#     assert item_c in ivette.inventory


# def test_swap_by_newest_reordered():
#     item_a = Decor(age=2.0)
#     item_b = Electronics(age=4.0)
#     item_c = Decor(age=4.0)
#     michelle = Vendor(
#         inventory=[item_c, item_b, item_a]
#     )

#     item_d = Clothing(age=2.0)
#     item_e = Decor(age=4.0)
#     item_f = Clothing(age=4.0)
#     ivette = Vendor(
#         inventory=[item_f, item_e, item_d]
#     )

#     result = michelle.swap_by_newest(
#         other=ivette,
#         my_priority="Clothing",
#         their_priority="Decor"
#     )

#     assert result
#     assert len(michelle.inventory) == 3
#     assert len(ivette.inventory) == 3
#     assert item_a in michelle.inventory
#     assert item_b in michelle.inventory
#     assert item_c not in michelle.inventory
#     assert item_f in michelle.inventory
#     assert item_d in ivette.inventory
#     assert item_e in ivette.inventory
#     assert item_f not in ivette.inventory
#     assert item_c in ivette.inventory


# def test_swap_by_newest_no_inventory_is_false():
#     michelle = Vendor(
#         inventory=[]
#     )

#     item_a = Clothing(age=2.0)
#     item_b = Decor(age=4.0)
#     item_c = Clothing(age=4.0)
#     ivette = Vendor(
#         inventory=[item_a, item_b, item_c]
#     )

#     result = michelle.swap_by_newest(
#         other=ivette,
#         my_priority="Clothing",
#         their_priority="Decor"
#     )

#     assert not result
#     assert len(michelle.inventory) == 0
#     assert len(ivette.inventory) == 3
#     assert item_a in ivette.inventory
#     assert item_b in ivette.inventory
#     assert item_c in ivette.inventory


# def test_swap_by_newest_no_other_inventory_is_false():
#     item_a = Clothing(age=2.0)
#     item_b = Decor(age=4.0)
#     item_c = Clothing(age=4.0)
#     michelle = Vendor(
#         inventory=[item_a, item_b, item_c]
#     )

#     ivette = Vendor(
#         inventory=[]
#     )

#     result = michelle.swap_by_newest(
#         other=ivette,
#         my_priority="Decor",
#         their_priority="Clothing"
#     )

#     assert not result
#     assert len(michelle.inventory) == 3
#     assert len(ivette.inventory) == 0
#     assert item_a in michelle.inventory
#     assert item_b in michelle.inventory
#     assert item_c in michelle.inventory


# def test_swap_by_newest_no_match_is_false():
#     item_a = Decor(age=2.0)
#     item_b = Electronics(age=4.0)
#     item_c = Decor(age=4.0)
#     michelle = Vendor(
#         inventory=[item_a, item_b, item_c]
#     )

#     item_d = Clothing(age=2.0)
#     item_e = Decor(age=4.0)
#     item_f = Clothing(age=4.0)
#     ivette = Vendor(
#         inventory=[item_d, item_e, item_f]
#     )

#     result = michelle.swap_by_newest(
#         other=ivette,
#         my_priority="Clothing",
#         their_priority="Clothing"
#     )

#     assert not result
#     assert len(michelle.inventory) == 3
#     assert len(ivette.inventory) == 3
#     assert item_a in michelle.inventory
#     assert item_b in michelle.inventory
#     assert item_c in michelle.inventory
#     assert item_d in ivette.inventory
#     assert item_e in ivette.inventory
#     assert item_f in ivette.inventory


# def test_swap_by_newest_no_other_match_is_false():
#     item_a = Decor(age=2.0)
#     item_b = Electronics(age=4.0)
#     item_c = Decor(age=4.0)
#     michelle = Vendor(
#         inventory=[item_c, item_b, item_a]
#     )

#     item_d = Clothing(age=2.0)
#     item_e = Decor(age=4.0)
#     item_f = Clothing(age=4.0)
#     ivette = Vendor(
#         inventory=[item_f, item_e, item_d]
#     )

#     result = michelle.swap_by_newest(
#         other=ivette,
#         my_priority="Electronics",
#         their_priority="Decor"
#     )

#     assert not result
#     assert len(michelle.inventory) == 3
#     assert len(ivette.inventory) == 3
#     assert item_a in michelle.inventory
#     assert item_b in michelle.inventory
#     assert item_c in michelle.inventory
#     assert item_d in ivette.inventory
#     assert item_e in ivette.inventory
#     assert item_f in ivette.inventory
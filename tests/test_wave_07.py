import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item

# for full disclosure I wrote these tests after I wrote the code, not before
# oops


def test_item_has_age():
    # Arrange
    item = Item(age=1)

    # Act
    # ?? not sure what should go here

    # Assert
    assert item.age == 1

def test_get_newest_item_with_optional_category_returns_newest_item_with_no_category():
    # Arrange
    item_a = Clothing(age=6)
    item_b = Decor(age=2)
    item_c = Clothing(age=4)
    item_d = Decor(age=5)
    item_e = Clothing(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )
    # Act
    newest_item = tai.get_newest_item_with_optional_category()

    # Assert
    assert newest_item == item_b

def test_newest_item_with_optional_category_returns_newest_item_in_category():
    # Arrange
    item_a = Clothing(age=6)
    item_b = Decor(age=2)
    item_c = Clothing(age=4)
    item_d = Decor(age=5)
    item_e = Clothing(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    # Act
    newest_clothing = tai.get_newest_item_with_optional_category("Clothing")

    # Assert
    newest_clothing = item_e

def test_swap_by_newest_swaps_newest_without_categories():
    
    # Arrange
    item_a = Decor(age=1)
    item_b = Electronics(age=2)
    item_c = Decor(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=4)
    item_e = Decor(age=5)
    item_f = Clothing(age=6)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    swapped = tai.swap_by_newest(jesse)

    # Assert
    assert swapped 
    assert item_a in jesse.inventory
    assert item_d in tai.inventory

def test_swap_by_newest_swaps_with_categories():
    # Arrange
    item_a = Decor(age=1)
    item_b = Electronics(age=2)
    item_c = Electronics(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=4)
    item_e = Decor(age=5)
    item_f = Decor(age=6)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    swapped = tai.swap_by_newest(jesse, "Decor", "Electronics")

    # Assert
    assert swapped
    assert item_b in jesse.inventory
    assert item_e in tai.inventory

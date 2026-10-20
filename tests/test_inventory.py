import pytest

from app.inventory import add_item, list_items
from app.validation import validate_item_name, validate_quantity


def test_add_and_list_item(tmp_path):
    path = tmp_path / "inventory.json"

    add_item("Mouse", 3, path)
    add_item("mouse", 2, path)

    assert list_items(path) == [
        {"name": "Mouse", "quantity": 5}
    ]


def test_reject_empty_name():
    with pytest.raises(ValueError):
        validate_item_name(" ")


def test_reject_negative_quantity():
    with pytest.raises(ValueError):
        validate_quantity(-1)


def test_reject_non_integer_quantity():
    with pytest.raises(ValueError):
        validate_quantity("dua")


def test_reject_boolean_quantity():
    with pytest.raises(ValueError):
        validate_quantity(True)
from app.storage import load_items, save_items
from app.validation import validate_item_name, validate_quantity


def add_item(name, quantity, path):
    name = validate_item_name(name)
    quantity = validate_quantity(quantity)

    items = load_items(path)

    for item in items:
        if item["name"].casefold() == name.casefold():
            item["quantity"] = (
                validate_quantity(item["quantity"]) + quantity
            )
            save_items(items, path)
            return item

    item = {"name": name, "quantity": quantity}
    items.append(item)
    save_items(items, path)

    return item


def list_items(path):
    return load_items(path)
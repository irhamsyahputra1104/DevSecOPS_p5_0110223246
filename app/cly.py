import argparse
from pathlib import Path

from app.inventory import add_item, list_items


def main():
    parser = argparse.ArgumentParser(
        description="Aplikasi inventaris sederhana"
    )

    commands = parser.add_subparsers(
        dest="command", required=True
    )

    add_parser = commands.add_parser("add")
    add_parser.add_argument("name")
    add_parser.add_argument("quantity", type=int)

    commands.add_parser("list")

    args = parser.parse_args()
    path = Path("inventory.json")

    if args.command == "add":
        item = add_item(args.name, args.quantity, path)
        print(f"Berhasil: {item['name']} - stok {item['quantity']}")
    else:
        items = list_items(path)

        if not items:
            print("Inventaris masih kosong.")

        for item in items:
            print(f"- {item['name']}: {item['quantity']}")


if __name__ == "__main__":
    main()
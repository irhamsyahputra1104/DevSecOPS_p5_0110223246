def validate_item_name(name):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Nama barang tidak boleh kosong.")

    if len(name.strip()) > 80:
        raise ValueError("Nama barang maksimal 80 karakter.")

    return name.strip()


def validate_quantity(quantity):
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise ValueError("Stok harus berupa bilangan bulat.")

    if quantity < 0:
        raise ValueError("Stok tidak boleh negatif.")

    return quantity
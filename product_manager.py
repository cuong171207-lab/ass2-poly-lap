def add_product(products):
    name = input("Tên sản phẩm: ")
    price = float(input("Giá sản phẩm: "))
    products.append({"name": name, "price": price})
    print("Đã thêm sản phẩm")


def remove_product(products, name):
    return [p for p in products if p["name"] != name]

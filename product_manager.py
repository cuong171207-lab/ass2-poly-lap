def add_product(products):
    name = input("Tên sản phẩm: ")
    price = float(input("Giá sản phẩm: "))
    products.append({"name": name, "price": price})
    print("Đã thêm sản phẩm")


def remove_product(products, name):
    return [p for p in products if p["name"] != name]
def remove_product(products, name):
    # remove product by name
    return [p for p in products if p["name"] != name]
def list_products(products):
    for p in products:
        print(p)
def list_products(products):
    if not products:
        print("No products")
    for p in products:
        print(p)
def update_price(product, new_price):
    product["price"] = new_price

products = [
    ["audi, 90"],
    ["bmw, 30"],
    ["tričko, 1"],
]
products2 = [
    {"name": "audi", "price": 50},
    {"name": "bmw", "price": 30},
]


def print_products():
    for product in products:
        print(f"Název produktu: {product[0]}, ")
    for product2 in products2:
        print(f"Název produktu: {product2['name']}, cena: {product2['price']}$")


def add_product():
    product_name = input("Název produktu: ")
    product_price = input("Název cenu: ")
    product = [product_name, product_price]
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product)


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky\n")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky")
        add_product()
        print("")
        menu()

    else:
        print("Něco jiného")
        menu()


menu()

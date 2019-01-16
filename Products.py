from decimal import *
"""
GetProductInfo()
ask for product name
validateName()
ask for product price
validatePrice()
ask for product quantity
validateQuantity()
ask for product locations
validateLocations()
create product object
"""


def validate_product_name(name_input):
    if name_input != "":
        return True
    else:
        return False


def validate_product_price(price_input):

    try:
        number = Decimal(price_input)
        number >= 0
        acceptable_number = True
    except InvalidOperation:
        acceptable_number = False

    return acceptable_number


def validate_product_quantity(quantity_input):
    try:
        number_quantity = int(quantity_input)
        acceptable_quantity = True
    except ValueError:
        acceptable_quantity = False

    return acceptable_quantity


def validate_product_locations(locations_input):
    if locations_input != "":
        return True
    else:
        return False


def get_user_product():

    name_accepted = False

    while not name_accepted:
        product_name_input = input("Please enter the product name. \n")
        name_accepted = validate_product_name(product_name_input)
        print("Name acceptable? " + str(name_accepted))
        product_name = product_name_input.strip()

    price_accepted = False

    while not price_accepted:
        product_price = input("Please enter the product price in integer or decimal format. \n")
        price_accepted = validate_product_price(product_price)
        print("Price acceptable? " + str(price_accepted))

    product_price_decimal = Decimal(product_price)

    quantity_accepted = False

    while not quantity_accepted:
        product_quantity = input("Please enter the product quantity as an integer. \n")
        quantity_accepted = validate_product_quantity(product_quantity)
        print("Quantity acceptable? " + str(quantity_accepted))

    product_quantity_int = int(product_quantity)

    locations_accepted = False

    while not locations_accepted:
        locations_input = input("Please Enter the product locations separated by commas. \n")
        locations_accepted = validate_product_locations(locations_input)
        print("Locations acceptable? " + str(locations_accepted))
        product_locations = list(map(str, (x.strip() for x in locations_input.split(","))))

    user_product = Product(product_name, product_price_decimal, product_quantity_int, product_locations)

    return user_product


"""
end GetProductInfo
"""


class Product:
    def __init__(self, name, price, quantity, locations):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.locations = locations


"""Greet user"""
print("Welcome to the Products program.")

"""GetProductInfo()"""
product = get_user_product()

print(product.name, product.price, product.quantity, product.locations)


"""

add product object to products collection

ask if want to add another product

if yes
    getProductInfo()
end if
else
    output to text file
    display message to user
    close program
end else
"""

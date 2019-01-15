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


def get_user_product():

    name_accepted = False

    while not name_accepted:
        product_name = input("Please enter the product name.")
        name_accepted = validate_product_name(product_name)
        print("Name acceptable?" + str(name_accepted))

    price_accepted = False

    while not price_accepted:
        product_price = input("Please enter the product price.")
        price_accepted = validate_product_price(product_price)
        print("Price acceptable?" + str(price_accepted))

    product_price_decimal = Decimal(product_price)

    product_quantity = input("Please enter the product quantity.")

    location_input = input("Enter the product locations separated by commas")
    product_locations = list(map(str, location_input.split(",")))

    """product_locations = input("Please enter the product locations.")"""

    user_product = Product(product_name, product_price_decimal, product_quantity, product_locations)

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

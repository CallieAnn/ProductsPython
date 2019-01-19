from decimal import *
import msvcrt

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


def get_product_name():
    name_accepted = False

    while not name_accepted:
        product_name_input = input("Please enter the product name. \n")
        name_accepted = validate_product_name(product_name_input)
        print("Name acceptable? " + str(name_accepted))

    product_name = product_name_input.strip()

    return product_name


def get_product_price():
    price_accepted = False

    while not price_accepted:
        product_price = input("Please enter the product price in integer or decimal format. \n")
        price_accepted = validate_product_price(product_price)
        print("Price acceptable? " + str(price_accepted))

    product_price_decimal = Decimal(product_price)

    return product_price_decimal


def get_product_quantity():
    quantity_accepted = False

    while not quantity_accepted:
        product_quantity = input("Please enter the product quantity as an integer. \n")
        quantity_accepted = validate_product_quantity(product_quantity)
        print("Quantity acceptable? " + str(quantity_accepted))

    product_quantity_int = int(product_quantity)

    return product_quantity_int


def get_product_locations():
    locations_accepted = False

    while not locations_accepted:
        locations_input = input("Please Enter the product locations separated by commas. \n")
        locations_accepted = validate_product_locations(locations_input)
        print("Locations acceptable? " + str(locations_accepted))

    product_locations = list(map(str, (x.strip() for x in locations_input.split(","))))

    return product_locations


def yes_or_no(question):
    user_answer = "invalid"
    while user_answer == "invalid":
        reply = str(input(question + ' (y/n): \n')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


def get_user_product():

    product_name = get_product_name()

    product_price = get_product_price()

    product_quantity = get_product_quantity()

    product_locations = get_product_locations()

    user_product = Product(product_name, product_price, product_quantity, product_locations)

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

    def product_to_string(self):
        return f"{self.name} \t\t ${self.price} \t\t" \
            f"{self.quantity} \t\t {self.locations}"


"""Greet user"""
print("Welcome to the Products program.")

"""GetProductInfo()"""
product = get_user_product()

print(product.product_to_string())

"""add product object to products collection"""
products = [product]

"""ask if want to add another product"""
another_product = yes_or_no("Would you like to add another product?")

"""if yes
    getProductInfo()
    add to products collection
end if"""
while another_product:
    additional_product = get_user_product()
    print(additional_product.product_to_string())
    products.append(additional_product)
    another_product = yes_or_no("Would you like to add another product?")

for p in products:
    print(p.product_to_string())

"""
else
    output to text file
    display message to user
    close program
end else
"""

file_name = input("Please enter a file name for your products. \n")

products_file = open(f"{file_name}.txt", "w")
products_file.write("Name \t\t Price \t\t Quantity \t\t Locations")
for p in products:
    products_file.write("\n")
    products_file.write(p.product_to_string())
products_file.close()

print(f"Your products are saved in {file_name}.txt ")

print("\n Press any key to exit.")
msvcrt.getch()
exit()


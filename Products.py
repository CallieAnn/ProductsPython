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


def get_user_product():
    product_name = input("Please enter the product name.")
    product_price = input("Please enter the product price.")
    product_quantity = input("Please enter the product quantity.")
    product_locations = input("Please enter the product locations.")

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

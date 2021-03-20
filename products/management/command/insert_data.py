from products.models import Product, Category
from data.off_parser import Parser


parser = Parser()
products = parser.main()
for code, product in products:
    print (product)

def insert_products(code, product):
    code = code
    name = product.get('name')
    brand = product.get('brand')
    nutriscore = product.get('nutriscore')
    add = Product(id = code, name = name, brand = brand, nutriscore = nutriscore)
    add.save()


def insert_categories():
    pass
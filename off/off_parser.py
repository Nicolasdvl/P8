from .open_food_facts import OFF_requests


class Parser():

    def main(self):
        off = OFF_requests()
        data = off.collect_data()
        valid_products = {}
        for page in data :
            products = data[page].get('products')
            if products is None:
                continue
            for product in products:
                if self.is_it_valid(product):
                    product = self.formate(product)
                    valid_products.update(product)
        return valid_products

    def is_it_valid(self, product:dict) -> bool:
        code = product.get('code')
        name = product.get('product_name_fr')
        brand = product.get('brands')
        nutriscore = product.get('nutriscore_grade')
        categories = product.get('categories_tags')
        image = product.get('image_url')

        if (name and code and brand and nutriscore and categories and image) is None:
            return False
        else:
            return True

    def formate(self, product):
        info_product = {}
        info_product['name'] = product.get('product_name_fr')
        info_product['brand'] = product.get('brands')
        info_product['nutriscore'] = product.get('nutriscore_grade')
        info_product['categories'] = product.get('categories_tags')
        info_product['image'] = product.get('image_url')
        result = {product.get('code'): info_product}
        return result


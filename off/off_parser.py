"""
Parse results from open_food_facts.py requests.

Check if data is valid and formate them in order to commit them in table.
"""
from .open_food_facts import OFF_requests
from progress.bar import ChargingBar


class Parser:
    """Contains functions that valid and formate data."""

    def main(self) -> dict:
        """Call functions to process the parsing."""
        off = OFF_requests()
        data = off.collect_data()
        print(f"from main, data = {data}")
        valid_products = {}
        bar = ChargingBar("Nettoyage des données... ")
        for page in data:
            products = data[page].get("products")
            if products is None:
                continue
            for product in products:
                print(f"from main, arg given to is_it_valid {product}")
                if self.is_it_valid(product):
                    product = self.formate(product)
                    valid_products.update(product)
            bar.next()
        bar.finish()
        print(f"from main, valid_products = {valid_products}")
        return valid_products

    def is_it_valid(self, product: dict) -> bool:
        """Return True if values wanted exists."""
        code = product.get("code")
        name = product.get("product_name_fr")
        brand = product.get("brands")
        nutriscore = product.get("nutriscore_grade")
        categories = product.get("categories_tags")
        image = product.get("image_url")

        if (
            name is None
            or code is None
            or brand is None
            or nutriscore is None
            or categories is None
            or image is None
        ):
            return False
        else:
            return True

    def formate(self, product: dict) -> dict:
        """
        Return formated dict populate with data.

        {
            int : {
                'name': str,
                'brand': str,
                'nutriscore': str,
                'categories': list,
                'image': str
            }
            ...
        }
        """
        info_product = {}
        info_product["name"] = product.get("product_name_fr")
        info_product["brand"] = product.get("brands")
        info_product["nutriscore"] = product.get("nutriscore_grade").upper()
        info_product["categories"] = product.get("categories_tags")
        info_product["image"] = product.get("image_url")
        result = {product.get("code"): info_product}
        return result

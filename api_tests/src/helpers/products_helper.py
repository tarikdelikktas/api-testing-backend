from api_tests.src.utilities.requestsUtility import RequestsUtility


class ProductsHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()

    def get_products_by_id(self, product_id):
        return self.request_utility.get(f"products/{product_id}")
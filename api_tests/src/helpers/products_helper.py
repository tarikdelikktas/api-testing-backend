from api_tests.src.utilities.requestsUtility import RequestsUtility


class ProductsHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()

    def get_products_by_id(self, product_id):
        return self.request_utility.get(f"products/{product_id}")

    def call_create_product(self, payload):
        return self.request_utility.post('products', payload=payload, expected_status_code=201)

    def call_list_all_products(self, payload=None):
        return self.request_utility.get('products', payload=payload)
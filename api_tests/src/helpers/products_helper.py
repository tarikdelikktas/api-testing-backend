from api_tests.src.utilities.requestsUtility import RequestsUtility
import logging as logger


class ProductsHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()

    def get_products_by_id(self, product_id):
        return self.request_utility.get(f"products/{product_id}")

    def call_create_product(self, payload):
        return self.request_utility.post('products', payload=payload, expected_status_code=201)

    def call_list_all_products(self, payload=None):

        max_pages = 1000
        all_products = []
        for i in range(1, max_pages, 1):
            logger.info(f"List products page number: {i}")

            if not 'per_page' in payload.keys():
                payload['per_page'] = 100

            #  add the current page number to the call
            payload['page'] = i
            rs_api = self.request_utility.get('products', payload=payload)

            #  if there is not response the stop the loop b/c there are no more products
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages.")

        return all_products

from api_tests.src.utilities.wooAPIUtility import WooAPIUtility
import os
import json


class OrdersHelper(object):

    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooAPIUtility()

    def create_order(self, additional_args=None):
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')
        # NOTE: in the data (create_order_payload.json) verify the product id used exists.   "line_items": [{"product_id": 18,"quantity": 1}
        # If the product does not exist you will get 'completed' as the default status of the order when created. The default should be 'processing'
        # if the product is valid.

        with open(payload_template) as f:
            payload = json.load(f)

        # if user adds more info to payload, then update it
        if additional_args:
            assert isinstance(additional_args,
                              dict), f"Parameter 'additional_args' must be a dictionary but found '{type(additional_args)}'"
            payload.update(additional_args)

        rs_api = self.woo_helper.post('orders', params=payload, expected_status_code=201)

        return rs_api
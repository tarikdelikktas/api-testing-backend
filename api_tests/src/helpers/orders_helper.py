from api_tests.src.utilities.wooAPIUtility import WooAPIUtility
from api_tests.src.dao.orders_dao import OrdersDAO
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

    @staticmethod
    def verify_order_is_created(order_json, exp_cust_id, exp_products):
        orders_dao = OrdersDAO()

        # verify response
        assert order_json, f"Create order response is empty"
        assert order_json['customer_id'] == exp_cust_id, (
            f"Create order with given customer id returned bad customer id."
            f"' Expected customer_id={exp_cust_id} but got '{order_json['customer_id']}'")
        assert len(order_json['line_items']) == len(exp_products), (
            f"Expected only {len(exp_products)} item in order but"
            f"found '{len(order_json['line_items'])}'"
            f"Order id: {order_json['id']}.")

        # verify DB
        order_id = order_json['id']
        line_info = orders_dao.get_order_lines_by_order_id(order_id)
        assert line_info, f"Create order line item not found in DB. Order id: {order_id}"

        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
        assert len(line_items) == 1, f"Expected 1 line item, but found {len(line_items)}. Ordder id: {order_id}."

        # get list of product ids in the response
        api_product_ids = [i['product_id'] for i in order_json['line_items']]

        for product in exp_products:
            assert product['product_id'] in api_product_ids, (
                f"Create order does not have at least 1 expected product in DB."
                f"Product id: {product['product_id']}. Order id: {order_id}")

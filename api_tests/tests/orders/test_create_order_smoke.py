from api_tests.src.dao.products_dao import ProductsDAO
from api_tests.src.helpers.orders_helper import OrdersHelper
import pytest

@pytest.mark.tcid8
def test_create_paid_order_guest_user():
    rand_dao = ProductsDAO()
    order_helper = OrdersHelper()

    # get a product from DB
    rand_product = rand_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    # make the API call
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]}
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    assert order_json, f"Create order response is empty"
    assert order_json['customer_id'] == 0, (f"Create order as guest as expected default"
                                            f"'customer_id=0 but got '{order_json['customer_id']}'")
    assert len(order_json['line_items']) == 1, (f"Expected only 1 item in order but"
                                                f"found '{len(order_json['line_items'])}'"
                                                f"Order id: {order_json['id']}.")
    
    # verify DB
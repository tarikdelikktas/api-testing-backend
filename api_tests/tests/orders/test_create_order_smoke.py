from api_tests.src.dao.products_dao import ProductsDAO
from api_tests.src.dao.orders_dao import OrdersDAO
from api_tests.src.helpers.orders_helper import OrdersHelper
import pytest

@pytest.mark.tcid8
def test_create_paid_order_guest_user():
    rand_dao = ProductsDAO()
    order_helper = OrdersHelper()
    orders_dao = OrdersDAO()

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
    order_id = order_json['id']
    line_info = orders_dao.get_order_lines_by_order_id(order_id)
    assert line_info,  f"Create order line item not found in DB. Order id: {order_id}"

    line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
    
    import pdb; pdb.set_trace()
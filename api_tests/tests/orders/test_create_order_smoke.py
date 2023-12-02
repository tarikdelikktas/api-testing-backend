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

    import pdb; pdb.set_trace()

    # verify response
    # verify DB
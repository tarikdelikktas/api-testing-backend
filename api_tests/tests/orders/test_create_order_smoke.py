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

    # make an API cal
    order_helper.create_order()

    # verify response
    # verify DB
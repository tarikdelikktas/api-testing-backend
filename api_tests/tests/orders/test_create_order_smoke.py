from api_tests.src.dao.products_dao import ProductsDAO
from api_tests.src.helpers.orders_helper import OrdersHelper
from api_tests.src.helpers.customers_helper import CustomerHelper
import pytest


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid8
def test_create_paid_order_guest_user():
    rand_dao = ProductsDAO()
    order_helper = OrdersHelper()

    customer_id = 0
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
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid9
def test_create_paid_order_new_created_customer():
    rand_dao = ProductsDAO()
    order_helper = OrdersHelper()
    customer_helper = CustomerHelper()

    # get a product from DB
    rand_product = rand_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    # make the API call
    cust_info = customer_helper.create_customer()
    customer_id = cust_info['id']

    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ],
        "customer_id": customer_id
    }
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)
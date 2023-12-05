from api_tests.src.dao.products_dao import ProductsDAO
from api_tests.src.helpers.orders_helper import OrdersHelper
from api_tests.src.helpers.customers_helper import CustomerHelper
import pytest


@pytest.fixture(scope='module')
def smoke_setup():
    product_dao = ProductsDAO()
    order_helper = OrdersHelper()
    customer_helper = CustomerHelper()

    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    info = {
        "product_id": product_id,
        "order_helper": order_helper,
        "customer_helper": customer_helper
    }
    return info


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid8
def test_create_paid_order_guest_user(smoke_setup):
    customer_id = 0
    product_id = smoke_setup['product_id']
    order_helper = smoke_setup['order_helper']

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
def test_create_paid_order_new_created_customer(smoke_setup):
    # create helper objects
    customer_helper = smoke_setup['customer_helper']
    product_id = smoke_setup['product_id']
    order_helper = smoke_setup['order_helper']

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

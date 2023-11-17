from api_tests.src.utilities.genericUtilities import generate_random_string
from api_tests.src.helpers.products_helper import ProductsHelper
from api_tests.src.dao.products_dao import ProductsDAO
import pytest


@pytest.mark.products
@pytest.mark.tcid6
def test_create_1_simple_product():
    # generate some data for the product
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # make the API call
    product_rs = ProductsHelper().call_create_product(payload)

    # verify the response is not empty
    assert product_rs, f"Create product API response is empty. Payload is: {payload}"
    assert product_rs['name'] == payload['name'], f"Create prodcct api call response has" \
                                                  f"unexpected name. Expected: {payload['name']}, Actual: {product_rs['name']}"

    # verify the response data in database
    product_id = product_rs['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title'], (f"Create product title in database does not match "
                                                            f"title in API. DB: {db_product['post_title']}, API: {payload['name']}")

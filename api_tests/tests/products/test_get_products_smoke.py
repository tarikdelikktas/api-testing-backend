import pytest
from api_tests.src.utilities.requestsUtility import RequestsUtility
from api_tests.src.dao.products_dao import ProductsDAO
from api_tests.src.helpers.products_helper import ProductsHelper


@pytest.mark.products
@pytest.mark.tcid4
def test_get_all_products():
    req_helper = RequestsUtility()
    rs_api = req_helper.get("products")

    assert rs_api, "Response of list all products is empty"


@pytest.mark.products
@pytest.mark.tcid5
def test_get_product_id_24():
    # get a product (test data) from database
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']

    # make API call and get response API
    product_helper = ProductsHelper()
    rs_api = product_helper.get_products_by_id(rand_product_id)
    api_name = rs_api['name']

    # verify the response --> [data in rand_product should match with data in rs_api]
    assert db_name == api_name, f"Get product by ud returned wrong product. Id: {rand_product_id}" \
                                f"DB Name: {db_name}, API Name: {api_name}"

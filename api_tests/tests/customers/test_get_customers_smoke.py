import pytest
import logging as logger
from api_tests.src.utilities.requestsUtility import RequestsUtility
@pytest.mark.customers
@pytest.mark.tcid2
def test_get_all_customers():
    req_helper = RequestsUtility()
    rs_api = req_helper.get('customers')

    assert rs_api, "Response of list all customers is empty"

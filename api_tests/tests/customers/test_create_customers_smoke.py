import pdb

import pytest
import logging as logger
from api_tests.src.utilities.genericUtilities import generate_random_email_and_password
from api_tests.src.helpers.customers_helper import CustomerHelper

@pytest.mark.tcid1
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only")

    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # import pdb; pdb.set_trace()
    # verify status code of the call

    # verify email in the response

    # verify customer is created in database
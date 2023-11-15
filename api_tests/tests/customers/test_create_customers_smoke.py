import pdb
import pytest
import logging as logger
from api_tests.src.utilities.genericUtilities import generate_random_email_and_password
from api_tests.src.helpers.customers_helper import CustomerHelper
from api_tests.src.dao.customers_dao import CustomersDAO


@pytest.mark.tcid1
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only.")

    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    # make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify email and first name in the response
    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '', f"Create customer api returned value for first_name" \
                                              f"but it should be empty."

    # verify customer is created in database
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)
    import pdb;
    pdb.set_trace()

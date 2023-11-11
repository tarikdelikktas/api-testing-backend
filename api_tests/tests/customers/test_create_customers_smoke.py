import pytest
import logging as logger
from api_tests.src.utilities.genericUtilities import generate_random_email_and_password

@pytest.mark.tcid1
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only")

    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    # create payload
    payload = {'email': email, 'password': password}

    # make the call

    # verify status code of the call

    # verify email in the response

    # verify customer is created in database
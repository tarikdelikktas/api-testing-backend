import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.mark.smoke
class TestCheckout(object):

    def test_checkout_as_guest(self):
        print("Checkout as guest")
        print("Function: Test11")

    def test_checkout_with_existing_user(self):
        print("Checkout with existing user")
        print("Function: test")
import pytest

pytestmark = [pytest.mark.fe, pytest.mark.slow]

@pytest.fixture(scope='module')
def setup():
    print("")
    print(">>> SETUP <<<")

    return {'id': 20, 'name': 'Tarik'}

@pytest.mark.abc
class TestCheckout(object):

    def test_checkout_as_guest(self, setup):
        print("Checkout as guest")
        print("Function: Test11")

    def test_checkout_with_existing_user(self, setup):
        print("Checkout with existing user")
        print("Function: test")

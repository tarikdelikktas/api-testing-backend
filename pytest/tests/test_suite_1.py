import pytest

pytestmark = [pytest.mark.be, pytest.mark.slow]

@pytest.fixture(scope='module')
def setup():
    print("")
    print(">>> SETUP <<<")

    return {'id': 20, 'name': 'Tarik'}

@pytest.mark.smoke
@pytest.mark.ll
def test_login_page_valid_user(setup):
    print("Login with valid user")
    print("Function: test1")
    print("Name: {}".format(setup.get('name')))
    # import pdb; pdb.set_trace()  # break point


@pytest.mark.regression
def test_login_page_wrong_password(setup):
    print("Login with wrong user")
    print("Function: test2")

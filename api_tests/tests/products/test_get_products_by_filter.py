from api_tests.src.helpers.products_helper import ProductsHelper
from api_tests.src.dao.products_dao import ProductsDAO
import pytest
from datetime import datetime, timedelta
import pdb

@pytest.mark.regression
class TestProductsWithFilter(object):

    @pytest.mark.tcid7
    def test_list_products_with_filter(self):

        # create data
        x_days_from_today = 30
        _after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = _after_created_date.isoformat()


        # Another way to create a date
        # tmp_date = datetime.now() - timedelta(days=x_days_from_today)
        # after_created_date = tmp_date.strftime('%Y-%M-%dT%H:%m:%S')

        # make the API call
        payload = dict()
        payload['after'] = after_created_date
        rs_api = ProductsHelper().call_list_all_products(payload)
        assert rs_api, f"Empty Response for 'list products with filter"

        # get the data from DB
        db_products = ProductsDAO().get_products_created_after_given_date(after_created_date)

        # verify response
        assert len(rs_api) == len(db_products), (f"List products with filters 'after' returned unexpected numberof products." \
                                                 f"Expected: {len(db_products)}, Actual: {len(rs_api)}")

        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]

        ids_diff = list(set(ids_in_api) - set(ids_in_db))
        assert not ids_diff, f"List products with filter, product ids in response mismatch in db."

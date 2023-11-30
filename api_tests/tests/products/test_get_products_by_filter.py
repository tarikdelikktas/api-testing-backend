from api_tests.src.helpers.products_helper import ProductsHelper
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
        pdb.set_trace()

        # get the data from DB
        # verify response
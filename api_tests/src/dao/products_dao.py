import random
from ..utilities.dbUtility import DBUtility


class ProductsDAO(object):
    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):
        sql = 'SELECT * FROM local.wp_posts WHERE post_type = "product" LIMIT 5000;'
        rs_sql = self.db_helper.execute_select(sql)
        return random.sample(rs_sql, int(qty))

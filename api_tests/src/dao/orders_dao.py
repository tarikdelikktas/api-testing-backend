from api_tests.src.utilities.dbUtility import DBUtility
class OrdersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_order_lines_by_order_id(self, order_id):
        sql = f'SELECT * FROM local.wp_woocommerce_order_items WHERE order_id = {order_id};'
        return self.db_helper.execute_select(sql)

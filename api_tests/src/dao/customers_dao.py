class CustomersDAO(object):
    def __init__(self):
        pass

    def get_customer_by_email(self, email):
        
        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}';"
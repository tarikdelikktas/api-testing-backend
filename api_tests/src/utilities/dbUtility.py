import pymysql
from api_tests.src.utilities.credentialsUtility import CredentialsUtility


class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialsUtility()
        self.creds = creds_helper.get_db_credentials()
        self.host = 'localhost'
        self.socket = "/Users/tarikdeliktas/Library/Application Support/Local/run/lz_eR5Rba/mysql/mysqld.sock"

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'],
                                     password=self.creds['db_password'],
                                     unix_socket=self.socket)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()
        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f'Failed running sql {sql} \n Error: {str(e)}')
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self, sql):
        pass

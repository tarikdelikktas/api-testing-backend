from api_tests.src.configs.hosts_config import API_HOSTS
import requests
import os
import json
from requests_oauthlib import OAuth1


class RequestsUtility(object):
    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1("ck_67ac45d287c3e936affb782c099203d06de749ac", "cs_c34948a934b1935f3ea94b08d311cba0e13362e4")

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        url = self.base_url + endpoint

        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers, auth=self.auth)
        self.status_code = rs_api.status_code
        assert self.status_code == int(expected_status_code), f'Expected status code {expected_status_code}, but actual {self.status_code}'
        return rs_api.json()

    def get(self):
        pass

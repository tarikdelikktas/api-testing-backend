import os
import json
class OrdersHelper(object):

    def __init__(self):

        # get path of current file
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))


    def create_order(self, additional_args=None):

        # get path of payload file relative to current file directory
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_template) as f:
            payload = json.load(f)

        import pdb; pdb.set_trace()

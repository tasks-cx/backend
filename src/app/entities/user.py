"""
username	=  <string>
domain		=  <host>
public-key	=  <path>

"""

import json

class User:
    def __init__(self, raw_str):
        json_obj = json.loads(raw_str)

        self.username = json_obj['username']
        self.domain = json_obj['domain']
        self.public_key = json_obj['public_key']

    def __str__(self):
        return f"User({self.username} {self.domain} {self.public_key})"

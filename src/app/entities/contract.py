"""
uuid			=  <uuid>
project-id		=  <uuid> @ <host>
member-id		=  <username> @ <hostname>
sign 			=  <sha256>
expiry			=  <timestamp>
links		        =  n * { <uri>, <label> }
witness 		=  1 * <sha265>
access			=  ?
"""

import json
import uuid
import datetime

from entities.primitives import ProjectId, UserId

class Contract:
    def __init__(self, raw_str):
        json_obj = json.loads(raw_str)

        self.uuid = uuid.UUID(json_obj['uuid'])
        self.project_id = ProjectId(json_obj['project_id'])
        self.member_id = UserId(json_obj['member_id'])
        self.sign = json_obj['sign']
        self.expiry = datetime.datetime.fromtimestamp(json_obj['expiry'], datetime.timezone.utc)
        self.witness = json_obj['witness'] # ?
        self.access = json_obj['access'] # ?


    def __str__(self):
        return f'Person(uuid: {self.uuid.hex}, project_id: {self.project_id}, member_id: {self.member_id}, sign: {self.sign}, expiry: {self.expiry}, witness: {self.witness}, access: {self.access})'

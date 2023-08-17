"""
project-id	        =  <uuid> “@” <host>
parent-project-id	=  <uuid> “@” <host> / NULL
title		        =  <string>
summary		        =  <string>
links		        =  n * { <uri>, <label> }
domain		        =  <host>
Creator		        =  <username> “@” <host>
owners		        =  <n> * <username> “@” <host>
members		        =  <n> * <username> “@” <host>
"""

import json
import uuid

from entities.primitives import ProjectId, ParentProjectId, Link, UserId
from entities.host import Host

class Project:
    def __init__(self, raw_str):
        json_obj = json.loads(raw_str)

        self.project_id = ProjectId(json_obj['project_id'])
        self.parent_project_id = ParentProjectId(json_obj['parent_project_id'])
        self.title = json_obj['title']
        self.summary = json_obj['summary']
        self.links = [Link(x) for x in json_obj['links']]
        self.domain = Host(json_obj['domain'])
        self.creator = UserId(json_obj['creator'])
        self.owners = [UserId(x) for x in json_obj['owners']]
        self.members = [UserId(x) for x in json_obj['members']]


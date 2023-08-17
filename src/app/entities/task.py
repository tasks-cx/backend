"""
uid			=  <uuid> “_” <project-id> “@” <host>
domain		        =  <host>
hash			=  <md5>
creator			=  <username> “@” <host>
project-id		=  <uuid> “@” <host>
parent-task-id		=  <project-id> “_” <uuid> “@” <host>
created		        =  <timestamp>
updated		        =  <timestamp>
title			=  <string>
status			=  <task-status>
links		        =  n * { <uri>, <label> }
assignee		=  <n> * <username> “@” <host> 
followers		=  <n> * <username> “@” <host>
due			=  <timestamp>
tags			=  <n> * <string>
body			=  <multipart>
attachments		=  <n> * <octet-stream>
comments		=  <n> * <multipart>
"""

import json
import datetime

from entities.primitives import ProjectId, Link, UserId, TaskId

class Task:
    def __init__(self, raw_str):
        json_obj = json.loads(raw_str)

        self.id = TaskId(json_obj['id'])
        self.domain = json_obj['domain']
        self.hash = json_obj['hash']
        self.creator = UserId(json_obj['creator'])
        self.project_id = ProjectId(json_obj['project_id'])
        self.parent_id = ProjectId(json_obj['parent_id'])
        self.created = json_obj['created']
        self.timestamp = json_obj['timestamp']
        self.title = json_obj['title']
        self.status = json_obj['status']
        self.links = [Link(x) for x in json_obj['links']]
        self.assignee = [UserId(x) for x in json_obj['assignee']]
        self.followers = [UserId(x) for x in json_obj['followers']]
        self.due = datetime.datetime.fromtimestamp(json_obj['due'], datetime.timezone.utc)
        self.tags = [x for x in json_obj['tags']]
        self.body = json_obj['body'] # TODO: call the multipart parser here
        self.attachment = json_obj['attachment'] # TODO: handle this as a byteArray or base64
        self.comments = [x for x in json_obj['comments']] # TODO: call the multipart parser here

    def __str__(self):
        return f"Task({self.id} {self.domain} {self.hash} {self.creator} {self.project_id} {self.parent_id} {self.created} {self.timestamp} {self.title} {self.status} {self.assignee} {self.followers} {self.due} {self.tags} {self.body} {self.attachment} {self.comments})"

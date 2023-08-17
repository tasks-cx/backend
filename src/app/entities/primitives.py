import uuid

from entities.host import Host

class ProjectId:
    def __init__(self, raw_str):
        raw_uuid, raw_host = raw_str.split('@')

        self.host = Host(raw_host)
        self.uuid = uuid.UUID(raw_uuid)

    def __str__(self):
        return f"{self.uuid.hex}@{self.host}"

class ParentProjectId:
    def __init__(self, raw_str):
        if raw_str:
            raw_uuid, raw_host = raw_str.split('@')
            self.uuid = uuid.UUID(raw_uuid)
            self.host = Host(raw_host)
        else:
            self.host = None
            self.uuid = None

    def __str__(self):
        return f"{self.uuid.hex}@{self.host}" if self.uuid else None

class TaskId:
    def __init__(self, raw_str):
        raw_uuid, rest = raw_str.split('_')
        raw_project_id, raw_host = rest.split('@')

        self.uuid = uuid.UUID(raw_uuid)
        self.project_id = ProjectId(raw_project_id)
        self.host = Host(raw_host)

    def __str__(self):
        return f"{self.uuid.hex}_{self.project_id}@{self.host}"


class UserId:
    def __init__(self, raw_str):
        self.username, self.host = raw_str.split('@')

    def __str__(self):
        return f"{self.username}@{self.host}"


class ParentId:
    def __init__(self, raw_str):
        raw_project_id, rest = raw_str.split('_')
        raw_uuid, raw_host = rest.split('@')

        self.project_id = ProjectId(raw_project_id)
        self.uuid = uuid.UUID(raw_uuid)
        self.host = Host(raw_host)

    def __str__(self):
        return f"{self.project_id}_{self.uuid.hex}@{self.host}"

class Link:
    def __init__(self, obj):
        self.label = obj['label']
        self.uri = obj['uri']
